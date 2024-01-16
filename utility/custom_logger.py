import logging
from pathlib import Path

root_logger = logging.getLogger()

format_string = "%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s"
consoleFormatter = logging.Formatter(format_string)

filename = "logs.log"
filename = Path() / filename
consoleHandler = logging.StreamHandler()
consoleFormatter.default_time_format = '%Y-%m-%d %H:%M:%S'
consoleFormatter.default_msec_format = '%s.%03d'
consoleHandler.setFormatter(consoleFormatter)
root_logger.addHandler(consoleHandler)

root_logger.setLevel("DEBUG")

