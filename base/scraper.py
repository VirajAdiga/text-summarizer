import re

from abc import ABC, abstractmethod
from loguru import logger


UNWANTED_SPACES_PATTERN = r"\s{2,}"


class Scraper(ABC):
    """
    Abstract base class for concrete scrapers
    """

    @abstractmethod
    def scrape_get_text_from_page(self, url):
        raise NotImplementedError

    def _clean_data(self, text):
        logger.info(f"Cleaning extracted data")
        return re.sub(UNWANTED_SPACES_PATTERN, " ", text).lstrip().rstrip()
