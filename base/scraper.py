from abc import ABC, abstractmethod


class Scraper(ABC):
    """
    Abstract base class for concrete scrapers
    """

    @abstractmethod
    def scrape_get_text_from_page(self, url):
        raise NotImplementedError
