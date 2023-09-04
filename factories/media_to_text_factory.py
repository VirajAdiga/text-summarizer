from media_to_text_converters.youtube_media_to_transcript_text import YoutubeMediaToTranscriptText


class MediaToTextConverterFactory:
    """
    Factory class to create required concrete media to text converter
    """

    @staticmethod
    def get_converter(converter_type):
        converter_map = {
            "youtube_media_transcript": YoutubeMediaToTranscriptText,
        }

        if converter_type not in converter_map:
            return None
        return converter_map[converter_type]()
