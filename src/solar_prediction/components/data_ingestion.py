import gdown,sys
from src.solar_prediction import logger,CustomException
from src.solar_prediction.config.configeration import ConfigurationManager
from src.solar_prediction.utils.common import create_directories

class DataIngestion:
    def __init__(self, config):
        self.config = config
        
    def download_file(self):
        try:
            
            create_directories(dir_path=[self.config.root_dir])
            
            #To download weather dataset
            dataset_url2 = self.config.source_url2
            output = self.config.local_weather_data
            gdown.download(dataset_url2, output, quiet=False)
            
            #to download generation dataset
            dataset_url1 = self.config.source_url1
            output = self.config.local_generation_data
            print(dataset_url1, output)
            gdown.download(dataset_url1, output, quiet=False)
            
        except Exception as e:
            raise CustomException(e,sys)
            

if __name__=="__main__":
    ingestion = DataIngestion(config=ConfigurationManager().config_validator())
    ingestion.download_file()









'''
# URL of the file to be downloaded
url = "https://drive.google.com/uc?id=15W2gIBC9KvNxOSNKPOsxB-9dn7FF9bQ-"
output = "downloaded_file.csv"  # specify the desired output file name
gdown.download(url, output, quiet=False)
'''