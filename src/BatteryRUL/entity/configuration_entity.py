from dataclasses import dataclass 
from pathlib import Path
import pymongo
from pymongo import MongoClient 
import pandas as pd
import os 

# Data Ingestion Entity 
@dataclass()
class DataIngestionConfig:
    root_dir: Path
    mongo_uri: str
    database_name: str
    collection_name: str


# Data validation entity 
@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    data_dir: Path
    all_schema: dict 

# Data Transformation entity 
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    numerical_cols: list
    categorical_cols: list
