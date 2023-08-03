from abc import ABC, abstractmethod


class Summarizer(ABC):
    """
    Abstract base class for concrete text summarizers
    """

    @abstractmethod
    def get_summarized_text(self, text_to_be_summarized):
        raise NotImplementedError
