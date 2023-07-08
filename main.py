import scraper
import summarizer

from loguru import logger


class Driver:
    scraper = scraper.Scraper()
    summarizer = summarizer.Summarizer()

    def get_text_from_page(self, page_url):
        logger.info(f"Initializing the scraper to extract data from page '{page_url}'")
        return self.scraper.scrape_get_text_from_page(page_url)

    def summarize_text(self, text):
        logger.info("Summarising text started")
        return self.summarizer.get_summarized_text(text)


def main(page_url):
    logger.info(f"Received request for scraping and summarising content from page '{page_url}'")
    driver = Driver()
    extracted_main_article = driver.get_text_from_page(page_url)
    logger.info(f"This is the full extracted content from the requested web page (Total length of chars: {len(extracted_main_article)}): \n{extracted_main_article}")
    summarised_content = driver.summarize_text(extracted_main_article)
    logger.info(f"This is the summarised content (Total length of chars: {len(summarised_content)}): \n{summarised_content}")


if __name__ == "__main__":
    url = "https://jamesclear.com/five-step-creative-process"
    main(url)
