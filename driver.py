import textwrap
import re

from loguru import logger

from factories.media_to_text_factory import MediaToTextConverterFactory
from factories.scraper_factory import ScraperFactory
from factories.summarizer_factory import SummarizerFactory
from constants import YOUTUBE_URL_REGEX_PATTERN


class Driver:

    def get_summary(self, url, max_length=None):
        logger.info(f"Received request for summarising content from '{url}'")

        regex_match = re.search(YOUTUBE_URL_REGEX_PATTERN, url)
        if regex_match:
            logger.info(f"Requested url is a youtube media")
            extracted_text = self._get_media_text(url)
        else:
            logger.info(f"Requested url is a web page")
            extracted_text = self._get_text_from_page(url)

        if extracted_text is None or len(extracted_text) < 1:
            logger.warning("There is no content to summarize from given url")
            return None

        # logger.info(f"This is the full extracted content from the requested web page (Total length of chars: {len(extracted_text)})")
        # logger.info(textwrap.fill(extracted_text, width=150))

        summarised_content = self._summarize_text(extracted_text, max_length)
        # logger.info(f"This is the summarised content (Total length of chars: {len(summarised_content)})")
        # logger.info(textwrap.fill(summarised_content, width=150))
        return summarised_content

    def _get_media_text(self, media_url):
        media_to_text_converter_type = "youtube_media_transcript"

        logger.info(f"Requested media to text converter type - {media_to_text_converter_type}")
        media_to_text_converter = MediaToTextConverterFactory.get_converter(media_to_text_converter_type)
        if media_to_text_converter is None:
            raise ValueError("Please specify a valid media to text converter")
        logger.info(f"Initializing the media to text converter to extract data from '{media_url}'")
        return media_to_text_converter.get_media_text(media_url)

    def _get_text_from_page(self, page_url):
        scraper_type = "goose"

        logger.info(f"Requested scraper type - {scraper_type}")
        scraper = ScraperFactory.get_scraper(scraper_type)
        if scraper is None:
            raise ValueError("Please specify a valid scraper")
        logger.info(f"Initializing the scraper to extract data from page '{page_url}'")
        return scraper.scrape_get_text_from_page(page_url)

    def _summarize_text(self, text, max_length):
        summarizer_type = "transformers"

        logger.info(f"Requested summarizer type - {summarizer_type}")
        summarizer = SummarizerFactory.get_summarizer(summarizer_type)
        if summarizer is None:
            raise ValueError("Please specify a valid summarizer")
        logger.info("Initializing the summarizer to summarize given text")
        return summarizer.get_summarized_text(text, max_length)
