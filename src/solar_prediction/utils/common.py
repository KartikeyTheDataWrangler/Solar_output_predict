import os
from box import ConfigBox
import yaml
import json
import joblib
import sys
from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
#import dill 
from solar_prediction import logger
from solar_prediction import CustomException

def read_yaml(yaml_path: Path):
    try:
        with open(yaml_path) as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_path} loaded successfully")
            return ConfigBox(yaml_content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e,sys)
    
    
    
def create_directories(dir_path: list):
    try:
        for path in dir_path:
            os.makedirs(path,exist_ok=True)
            logger.info(f"created directory at : {path}")  
    except Exception as e:
        raise CustomException(e,sys) 
        
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"saving object {obj} in location {file_path}")
        with open(file_path, "wb") as file_obj:
            joblib.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)
    

def read_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            obj = joblib.load(file_obj)
        return obj
    except Exception as e:
        raise CustomException(e,sys)


if __name__=="__main__":
    con = read_yaml(yaml_path="config\config.yaml")
    de = con.data_ingestion
    print(de.root_dir)