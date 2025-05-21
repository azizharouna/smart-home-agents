import logging
from datetime import datetime

def configure_logging():
    """Set up structured logging for the system"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"logs/smart_home_{datetime.now().strftime('%Y%m%d')}.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)

class PerformanceLogger:
    """Helper class for performance metrics logging"""
    def __init__(self, logger):
        self.logger = logger

    def log_metric(self, name: str, value: float):
        self.logger.info(f"METRIC|{name}|{value}")