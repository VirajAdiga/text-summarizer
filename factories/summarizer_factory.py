from summarizers.extractive_summarizer import ExtractiveSummarizer
from summarizers.textrank_summarizer import TextrankSummarizer


class SummarizerFactory:
    """
    Factory class to create required concrete text summarizers
    """

    @staticmethod
    def get_summarizer(summarizer_type):
        summarizer_map = {
            "extractive": ExtractiveSummarizer,
            "textrank": TextrankSummarizer
        }

        if summarizer_type not in summarizer_map:
            return None
        return summarizer_map[summarizer_type]()
