from solar_prediction import logger
from box import ConfigBox
logger.info("welcome")
from src.solar_prediction.pipelines import training_pipeline


def train_base_model_only():
    training_pipeline()

