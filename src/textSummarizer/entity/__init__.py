from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_name: str  # Added this to hold the HF ID
    local_data_file: Path
    unzip_dir: Path