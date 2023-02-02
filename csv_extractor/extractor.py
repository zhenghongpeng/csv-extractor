
from threading import Event

from cognite.client import CogniteClient
from cognite.extractorutils.statestore import AbstractStateStore

from csv_extractor.config import Config


def run_extractor(cognite: CogniteClient, states: AbstractStateStore, config: Config, stop_event: Event) -> None:
    print("Hello, world!")
