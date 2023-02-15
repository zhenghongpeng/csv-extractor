import logging
import os
import stat
from csv import DictReader
from threading import Event

from cognite.client import CogniteClient
from cognite.client.data_classes import Row
from cognite.extractorutils.statestore import AbstractStateStore
from cognite.extractorutils.uploader import RawUploadQueue

from csv_extractor.config import Config, FileConfig

logger = logging.getLogger()

def extract_file(file: FileConfig, queue: RawUploadQueue) -> None:

    logger.info(f"Extracting {file.path}")
    with open(file.path) as infile:
        reader = DictReader(infile)

        for row in reader:
            queue.add_to_upload_queue(
                database=file.destination.database,
                table=file.destination.table,
                raw_row=Row(key=row[file.key_column], columns=row)
            )
def run_extractor(cognite: CogniteClient, states: AbstractStateStore, config: Config, stop_event: Event) -> None:

    with RawUploadQueue(cdf_client=cognite, max_queue_size=100_000) as queue:
        for file in config.files:
            if stop_event.is_set():
                break
            previous_version = states.get_state(file.path)[1] or 0
            new_version = os.stat(file.path)[stat.ST_MTIME]
            if new_version > previous_version:
                extract_file(file, queue)
                states.expand_state(file.path, high=new_version)
            else:
                logger.info(f"{file.path} has not changed, skipping")
