from summarizers.extractive_summarizer import ExtractiveSummarizer


class SummarizerFactory:
    """
    Factory class to create required concrete text summarizers
    """

    @staticmethod
    def get_summarizer(summarizer_type):
        summarizer_map = {
            "extractive": ExtractiveSummarizer
        }

        if summarizer_type not in summarizer_map:
            return None
        return summarizer_map[summarizer_type]()
