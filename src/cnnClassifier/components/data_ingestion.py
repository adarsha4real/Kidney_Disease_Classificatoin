import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self)->str:
        logger.info(f"msg=Downloading file from :[{self.config.source_URL}] to :[{self.config.local_data_file}]")

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"download started")
            file_id=dataset_url.split('/')[-2]
            prefix = "https://drive.google.com/uc?id="
            gdown.download(prefix + file_id, zip_download_dir)
            logger.info(f"download completed successfully")
        except Exception as e:
            logger.error(f"error occurred while downloading file: {e}")
            raise e

    def extract_zip_file(self):
        logger.info(f"msg=Extracting zip file :[{self.config.local_data_file}]")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)