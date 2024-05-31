import sys
from solar_prediction import logger,CustomException
from solar_prediction.config.configeration import ConfigurationManager
from solar_prediction.utils.common import create_directories, save_object
import pandas as pd

class DataTransformation:
    def __init__(self, config):
        self.config = config
        
    def read_datasets(self):
        try:
            df = pd.read_csv(self.config.local_weather_data)
            print(df)
        except Exception as e:
            raise CustomException(e,sys)
    
        
            
if __name__=="__main__":
    transformer = DataTransformation(config=ConfigurationManager().data_transformer_validated())
    transformer.read_datasets()
    save_object(obj=transformer.read_datasets(),file_path=ConfigurationManager().data_transformer_validated().transformer_obj_path)
    