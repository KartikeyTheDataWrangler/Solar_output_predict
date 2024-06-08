import sys
from src.solar_prediction import logger,CustomException
from src.solar_prediction.config.configeration import ConfigurationManager
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from src.solar_prediction.utils.common import save_object, read_object
import mlflow, os
from dotenv import load_dotenv

load_dotenv('.env')
class ModelTRainer:
    def __init__(self, config):
        self.config = config
    
    def train_base_model(self):
        try:
            df = pd.read_csv(self.config.transformed_data_path)
          
            X = df[['DAILY_YIELD','TOTAL_YIELD','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','DC_POWER']]
            y = df['AC_POWER']
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
            #print(X_train, y_train)
            
            rfr = RandomForestRegressor()
           
            
            param_rf = {
            'n_estimators': [50],
                'max_depth': [8,10 ],
            'min_samples_leaf': [12,15],
                'criterion' :['squared_error', 'squared_error'],
                }
            grid_search = GridSearchCV(estimator=rfr, param_grid=param_rf, cv=2, n_jobs=-1)
            grid_search.fit(X_train, y_train)

            best_model = grid_search.best_estimator_
            
            save_object(file_path=self.config.saved_base_model_path,obj=best_model)
            logger.info('Best Model Saved succesfully')
            return X_test, y_test
        
        except Exception as e:
            CustomException(e,sys)
                
    def mlflow_dagshub_logging(self,X_test,y_test):
        try:
            DAGSHUB_USER = os.getenv('MLFLOW_TRACKING_USERNAME')
            DAGS_URI = os.getenv('MLFLOW_TRACKING_URI ')
            exp = mlflow.set_experiment(experiment_name='solar_panel_prediction')
            mlflow.set_tracking_uri(DAGS_URI)
            model_path = self.config.saved_base_model_path
            model = read_object(file_path=model_path)
            logger.info('best model loaded succesfully')
            with mlflow.start_run():
                pred = model.predict(X_test)
                mse = mean_squared_error(y_test, pred)
                r2 = r2_score(y_test, pred)
                
                metrics = {"mse":mse, "r2": r2}
                
                mlflow.log_metrics(metrics)
                mlflow.log_params(model.get_params())
            
        except Exception as e:
            CustomException(e,sys)
       
 
 
if __name__=="__main__":  
    train_model = ModelTRainer(config=ConfigurationManager().model_trainer_validated())
    X_test, y_test = train_model.train_base_model()
    train_model.mlflow_dagshub_logging(X_test, y_test)
  