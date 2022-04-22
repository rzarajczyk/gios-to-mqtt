import logging
from logging import config as logging_config

import yaml
import os


def start_service():
    with open("logging.yaml", 'r') as f:
        config = yaml.full_load(f)
    logging_config.dictConfig(config)

    logger = logging.getLogger("main")
    logger.info("Starting application!")

    config_file = os.getenv('CONFIG', 'config/config.yaml')

    with open(config_file, 'r') as f:
        config = yaml.full_load(f)

    return config, logger
