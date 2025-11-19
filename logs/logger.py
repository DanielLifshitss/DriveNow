import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging() -> logging.Logger:
    log_file = Path("logs/app.log")
    logger = logging.getLogger("vehicle_app")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    fh = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
