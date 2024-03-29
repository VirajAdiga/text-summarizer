import re

from loguru import logger
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from base.media_to_text import MediaToText

from constants import YOUTUBE_URL_REGEX_PATTERN


class YoutubeMediaToTranscriptText(MediaToText):
    """
    Concrete scraper for getting YouTube transcript text
    """

    def get_media_text(self, media_url):
        regex_match = re.search(YOUTUBE_URL_REGEX_PATTERN, media_url)
        video_id = regex_match.group(1)

        logger.info("Getting transcript data")

        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        except TranscriptsDisabled:
            logger.warning("Transcripts are disabled for the given media")
            return None

        logger.info("Generating transcript text with the help of transcript data")
        transcript_text = ""

        for data in transcript_data:
            text = data.get('text', None)
            if text and text != '[Music]':
                transcript_text += " " + text

        logger.info("Transcript is ready to be picked up")
        return self._clean_data(transcript_text)
