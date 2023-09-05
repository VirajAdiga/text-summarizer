import re

from abc import ABC, abstractmethod
from loguru import logger


UNWANTED_SPACES_PATTERN = r"\s{2,}"


class MediaToText(ABC):
    """
    Abstract base class for concrete media to text converter
    """

    @abstractmethod
    def get_media_text(self, media_url):
        raise NotImplementedError

    def _clean_data(self, text):
        logger.info(f"Cleaning extracted data")
        return re.sub(UNWANTED_SPACES_PATTERN, " ", text).lstrip().rstrip()
