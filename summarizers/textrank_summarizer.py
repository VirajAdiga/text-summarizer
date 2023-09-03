import spacy
import pytextrank

from loguru import logger

from base.summarizer import Summarizer


class TextrankSummarizer(Summarizer):
    """
    Concrete summarizer using spacy
    """

    def get_summarized_text(self, text_to_be_summarized, max_length=None):

        # Initialize spacy pipline
        logger.info("Initializing spacy pipeline")
        spacy_pipeline = spacy.load("en_core_web_lg")

        # Add text rank to pipeline
        spacy_pipeline.add_pipe("textrank")

        logger.info("Generating summary")
        summarized = spacy_pipeline(text_to_be_summarized)
        summary = ''
        for sentence in summarized._.textrank.summary():
            summary += " " + sentence.text

        logger.info("Summary is ready to be picked up")
        return summary.lstrip().rstrip()
