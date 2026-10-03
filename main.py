from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.constants import *
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
        




