import logging
import os
from config import LOG_FILE


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"
    )

    logger = logging.getLogger()
    return logger