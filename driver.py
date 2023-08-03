from loguru import logger

from factories.scraper_factory import ScraperFactory
from factories.summarizer_factory import SummarizerFactory


class Driver:

    @staticmethod
    def get_text_from_page(page_url, scraper_type):
        scraper = ScraperFactory.get_scraper(scraper_type)
        if scraper is None:
            raise ValueError("Please specify a valid scraper")
        logger.info(f"Initializing the scraper to extract data from page '{page_url}'")
        return scraper.scrape_get_text_from_page(page_url)

    @staticmethod
    def summarize_text(text, summarizer_type):
        summarizer = SummarizerFactory.get_summarizer(summarizer_type)
        if summarizer is None:
            raise ValueError("Please specify a valid summarizer")
        logger.info("Summarising text started")
        return summarizer.get_summarized_text(text)
