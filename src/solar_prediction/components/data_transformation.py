import sys
from solar_prediction import logger,CustomException
from solar_prediction.config.configeration import ConfigurationManager
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class DataTransformation:
    def __init__(self, config):
        self.config = config
        
    def merge_transform_datasets(self):
        try:
            df_weather = pd.read_csv(self.config.local_weather_data)
            df_generation = pd.read_csv(self.config.local_generation_data)
            #print(df_generation, df_weather)
            
            df_solar = pd.merge(df_generation.drop(columns = ['PLANT_ID']), df_weather.drop(columns = ['PLANT_ID', 'SOURCE_KEY']), on='DATE_TIME')
            df_solar['DATE_TIME'] = pd.to_datetime(df_solar['DATE_TIME'])
            df_solar['DAY'] = df_solar['DATE_TIME'].dt.day
            df_solar['MONTH'] = df_solar['DATE_TIME'].dt.month
            
            encoder = LabelEncoder()
            df_solar['SOURCE_KEY_NUMBER'] = encoder.fit_transform(df_solar['SOURCE_KEY'])
            df_solar.to_csv(path_or_buf=self.config.transformed_data_path)
            print(df_solar)
        except Exception as e:
            raise CustomException(e,sys)
    
       
            
if __name__=="__main__":
    transformer = DataTransformation(config=ConfigurationManager().data_transformer_validated())
    transformer.merge_transform_datasets()
    