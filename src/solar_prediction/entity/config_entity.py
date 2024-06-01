from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url1: str
    source_url2: str
    local_generation_data: Path
    local_weather_data: Path
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    transformed_data_path: Path
    local_generation_data: Path
    local_weather_data: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    transformed_data_path: Path
    saved_model_path: Path
   
   
  