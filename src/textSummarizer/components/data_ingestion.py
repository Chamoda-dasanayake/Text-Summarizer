import os
from datasets import load_dataset
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Instead of downloading a zip, this loads the dataset 
        from Hugging Face and saves it to your artifacts folder.
        """
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading dataset {self.config.dataset_name} from Hugging Face...")
            
            # This fetches the dataset (SAMSum)
            dataset = load_dataset(self.config.dataset_name)
            
            # Save it to your local directory (e.g., artifacts/data_ingestion)
            dataset.save_to_disk(self.config.root_dir)
            logger.info(f"Dataset saved successfully at: {self.config.root_dir}")
        else:
            logger.info(f"Dataset already exists at: {self.config.local_data_file}")

    def extract_zip_file(self):
        """
        Since we are downloading directly via 'datasets' library, 
        we don't need to unzip anything anymore! 
        I'm keeping this here so your pipeline doesn't break.
        """
        logger.info("Using Hugging Face format; skipping zip extraction.")
        pass