from dataclasses import dataclass
from pathlib import Path
from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.logging import logger

from src.textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_filepath)
        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        cfg = self.config.data_ingestion
        create_directories([Path(cfg.root_dir), Path(cfg.unzip_dir)])
        return DataIngestionConfig(
            root_dir=Path(cfg.root_dir),
            dataset_name=cfg.dataset_name,
            local_data_file=Path(cfg.local_data_file),
            unzip_dir=Path(cfg.unzip_dir),
        )