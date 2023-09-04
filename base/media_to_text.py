from abc import ABC, abstractmethod


class MediaToText(ABC):
    """
    Abstract base class for concrete media to text converter
    """

    @abstractmethod
    def get_media_text(self, media_url):
        raise NotImplementedError
