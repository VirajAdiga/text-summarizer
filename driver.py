from loguru import logger

from factories.scraper_factory import ScraperFactory
from factories.summarizer_factory import SummarizerFactory


class Driver:

    def get_summary_of_page(self, page_url, scraper_type="goose", summarizer_type="extractive"):
        logger.info(f"Received request for scraping and summarising content from page '{page_url}'")
        extracted_main_article = self._get_text_from_page(page_url, scraper_type)
        logger.info(f"This is the full extracted content from the requested web page (Total length of chars: {len(extracted_main_article)}): \n{extracted_main_article}")
        summarised_content = self._summarize_text(extracted_main_article, summarizer_type)
        logger.info(f"This is the summarised content (Total length of chars: {len(summarised_content)}): \n{summarised_content}")
        return summarised_content

    def _get_text_from_page(self, page_url, scraper_type):
        scraper = ScraperFactory.get_scraper(scraper_type)
        if scraper is None:
            raise ValueError("Please specify a valid scraper")
        logger.info(f"Initializing the scraper to extract data from page '{page_url}'")
        return scraper.scrape_get_text_from_page(page_url)

    def _summarize_text(self, text, summarizer_type):
        summarizer = SummarizerFactory.get_summarizer(summarizer_type)
        if summarizer is None:
            raise ValueError("Please specify a valid summarizer")
        logger.info("Summarising text started")
        return summarizer.get_summarized_text(text)
