
from dataclasses import dataclass
from typing import List

from cognite.extractorutils.configtools import BaseConfig, StateStoreConfig, RawDestinationConfig


@dataclass
class ExtractorConfig:
    state_store: StateStoreConfig = StateStoreConfig()

@dataclass
class FileConfig:
    path: str
    key_column: str
    destination: RawDestinationConfig

@dataclass
class Config(BaseConfig):
    files: List[FileConfig]
    extractor: ExtractorConfig = ExtractorConfig()
