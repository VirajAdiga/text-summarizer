from loguru import logger

from driver import Driver


def main(page_url, scraper_type="goose", summarizer_type="extractive"):
    logger.info(f"Received request for scraping and summarising content from page '{page_url}'")
    extracted_main_article = Driver.get_text_from_page(page_url, scraper_type)
    logger.info(f"This is the full extracted content from the requested web page (Total length of chars: {len(extracted_main_article)}): \n{extracted_main_article}")
    summarised_content = Driver.summarize_text(extracted_main_article, summarizer_type)
    logger.info(f"This is the summarised content (Total length of chars: {len(summarised_content)}): \n{summarised_content}")


if __name__ == "__main__":
    url = "https://jamesclear.com/saying-no"
    main(url)
