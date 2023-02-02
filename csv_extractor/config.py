
from dataclasses import dataclass

from cognite.extractorutils.configtools import BaseConfig, StateStoreConfig


@dataclass
class ExtractorConfig:
    state_store: StateStoreConfig = StateStoreConfig()


@dataclass
class Config(BaseConfig):
    extractor: ExtractorConfig = ExtractorConfig()
