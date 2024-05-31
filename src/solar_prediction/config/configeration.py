import os, sys
from solar_prediction.constants import *
from solar_prediction.utils.common import read_yaml, create_directories
from solar_prediction.entity.config_entity import (DataIngestionConfig, DataTransformationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        #self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        
    def config_validator(self) -> DataIngestionConfig:
        config_yaml_values = self.config.data_ingestion
        
        data_ingestion_validated = DataIngestionConfig(
            root_dir=config_yaml_values.root_dir,
            source_url1=config_yaml_values.source_url1,
            source_url2=config_yaml_values.source_url2,
            local_generation_data=config_yaml_values.local_generation_data,
            local_weather_data=config_yaml_values.local_weather_data,
            )    
        return data_ingestion_validated

    def data_transformer_validated(self) -> DataTransformationConfig:
        config_yaml_values = self.config.data_transformer
        
        transformer_validated = DataTransformationConfig(
            root_dir=config_yaml_values.root_dir,
            transformer_obj_path=config_yaml_values.transformer_obj_path,
            local_generation_data=config_yaml_values.local_generation_data,
            local_weather_data=config_yaml_values.local_weather_data,
        )
        return transformer_validated





    
if __name__=="__main__":
    val = ConfigurationManager().config_validator()
    print(val)
