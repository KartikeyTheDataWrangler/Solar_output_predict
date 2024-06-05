import gdown,sys
from src.solar_prediction import logger,CustomException
from src.solar_prediction.config.configeration import ConfigurationManager
from src.solar_prediction.components.data_ingestion import DataIngestion
from src.solar_prediction.components.data_transformation import DataTransformation
from src.solar_prediction.components.model_tranier import ModelTRainer

logger.info(">>>>>>>>> Data Ingestion Started <<<<<<<<<<<")
ingestion_cofig = ConfigurationManager().config_validator()
make_ingestion = DataIngestion(config=ingestion_cofig)
make_ingestion.download_file()

logger.info(">>>>>>>>> Data Transformation Started <<<<<<<<<<<")
transformation_config = ConfigurationManager().data_transformer_validated()
make_transformer = DataTransformation(config=transformation_config)
make_transformer.merge_transform_datasets()

logger.info(">>>>>>>>> Model Trainer Started <<<<<<<<<<<")
model_trainer_config = ConfigurationManager().model_trainer_validated()
make_model_trainer = ModelTRainer(config=model_trainer_config)
X_test, y_test = make_model_trainer.train_base_model()
make_model_trainer.mlflow_dagshub_logging(X_test, y_test)


