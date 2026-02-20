import logging
import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    os.makedirs("reports/logs", exist_ok=True)
    logger = logging.getLogger("wikipedia")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    file_handler = logging.FileHandler("reports/logs/test.log")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.propagate = False
    logger.info("LOGGER INITIALIZED")
