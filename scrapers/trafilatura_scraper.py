import trafilatura

from loguru import logger

from base.scraper import Scraper


class TrafilaturaScraper(Scraper):
    """
    Concrete scraper using trafilatura
    """

    def scrape_get_text_from_page(self, url):
        logger.info(f"Sending request to page '{url}'")
        downloaded = trafilatura.fetch_url(url)
        logger.info(f"Extracting the response")
        downloaded = trafilatura.extract(downloaded)
        return self._clean_data(downloaded)
