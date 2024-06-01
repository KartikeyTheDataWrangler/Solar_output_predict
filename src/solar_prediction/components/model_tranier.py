import sys
from solar_prediction import logger,CustomException
from solar_prediction.config.configeration import ConfigurationManager
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class ModelTRainer:
    def __init__(self, config):
        self.config = config
        
    def mlflow_dagshub_logging():
        pass 