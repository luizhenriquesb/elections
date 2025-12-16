import logging

logger = logging.getLogger()
logger.handlers.clear()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M"
)

# Console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Arquivo
file_handler = logging.FileHandler("pipeline.txt", mode="w")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)