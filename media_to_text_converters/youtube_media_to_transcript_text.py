from loguru import logger

from base.media_to_text import MediaToText


class YoutubeMediaToTranscriptText(MediaToText):
    """
    Concrete scraper for getting YouTube transcript text
    """

    def get_media_text(self, media_url):
        pass
