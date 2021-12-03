import logging

logger = logging.getLogger(__name__)

level = logging.DEBUG
handler = logging.FileHandler("risteys.log")
formatter = logging.Formatter(
    "%(asctime)s %(levelname)-8s %(module)-21s %(funcName)-25s: %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(level)
