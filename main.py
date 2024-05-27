from src.BatteryRUL import logging
from src.BatteryRUL.pipelines.pip_01_data_ingestion import DataIngestionPipeline


COMPONENT_01_NAME = "Data Ingestion Component"
try:
    logging.info(f"# ======================{COMPONENT_01_NAME} Started! ================================= #")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logging.info(f"## ========================{COMPONENT_01_NAME} Terminated Successfully!======================= ##\n\nx******************x")

except Exception as e:
    logging.exception(e)
    raise e