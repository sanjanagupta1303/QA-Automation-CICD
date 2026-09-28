import logging
import os


# Create logs folder
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("QA-Automation")
logger.setLevel(logging.INFO)

# Prevent duplicate log messages
logger.propagate = False

# Avoid adding handlers multiple times
if not logger.handlers:

    # File handler
    file_handler = logging.FileHandler(
        "logs/test_execution.log",
        mode="a",
        encoding="utf-8"
    )

    # Console handler
    console_handler = logging.StreamHandler()

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)