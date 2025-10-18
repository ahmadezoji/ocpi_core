import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

class Logger:
    """
    Reusable logger supporting multiple levels and rotating file output.
    Example:
        log = Logger("ocpp_service").get_logger()
        log.info("Server started")
        log.error("Connection failed")
    """
    def __init__(self, name: str, log_dir: str = "logs", max_bytes: int = 5 * 1024 * 1024, backup_count: int = 5):
        self.name = name
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

        log_filename = os.path.join(log_dir, f"{name}_{datetime.now():%Y-%m-%d}.log")
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Capture all levels; filter by handler if needed

        if not self.logger.handlers:  # Avoid duplicate handlers on reload
            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            # File Handler (rotating logs)
            file_handler = RotatingFileHandler(log_filename, maxBytes=max_bytes, backupCount=backup_count)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
