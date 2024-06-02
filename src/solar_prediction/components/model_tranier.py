import sys
from solar_prediction import logger,CustomException
from solar_prediction.config.configeration import ConfigurationManager
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from solar_prediction.utils.common import save_object

class ModelTRainer:
    def __init__(self, config):
        self.config = config
    
    def train_base_model(self):
        try:
            df = pd.read_csv(self.config.transformed_data_path)
          
            X = df[['DAILY_YIELD','TOTAL_YIELD','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','DC_POWER']]
            y = df['AC_POWER']
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
            print(X_train, y_train)
            
            rfr = RandomForestRegressor()
            model = rfr.fit(X_train, y_train)
            pred = model.predict(X_test)
            
            mse = mean_squared_error(y_test, pred)
            r2 = r2_score(y_test, pred)
            
            save_object(file_path=self.config.saved_base_model_path,obj=model)
            print(mse, r2)
            
        
        except Exception as e:
            CustomException(e,sys)
            
        
        
        
                
    def mlflow_dagshub_logging(self):
       print(self.config) 
       pass 
 
 
if __name__=="__main__":  
    train_model = ModelTRainer(config=ConfigurationManager().model_trainer_validated())
    train_model.train_base_model()