from src.BatteryRUL.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.BatteryRUL.utils.commons import read_yaml, create_directories
from src.BatteryRUL.entity.configuration_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig)
from pathlib import Path

# Creating a ConfigurationManager class to manage configurations
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH):

        """Initialize ConfigurationManager."""
        # Read YAML configuration files to initialize configuration parameters
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Create necessary directories specified in the configuration
        create_directories([self.config.artifacts_root])

# Data Ingestion Config
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Get data ingestion configuration."""
        # Get data ingestion section from config
        config = self.config.data_ingestion

        # Create DataIngestionConfig object
        create_directories([config.root_dir])

        # Create and return DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            mongo_uri=config.mongo_uri,
            database_name=config.database_name,
            collection_name=config.collection_name,
        )

        return data_ingestion_config
    
# Data Validation Config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation 
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            data_dir=config.data_dir,
            all_schema=schema
        )
        return data_validation_config

# Data Transformation Config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            numerical_cols=list(config.numerical_cols),
            categorical_cols=list(config.categorical_cols)
        )
        return data_transformation_config