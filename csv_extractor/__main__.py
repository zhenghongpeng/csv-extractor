
from cognite.extractorutils import Extractor

from csv_extractor import __version__
from csv_extractor.extractor import run_extractor
from csv_extractor.config import Config


def main() -> None:
    with Extractor(
        name="csv_extractor",
        description="csv extractor",
        config_class=Config,
        run_handle=run_extractor,
        version=__version__,
    ) as extractor:
        extractor.run()


if __name__ == "__main__":
    main()
