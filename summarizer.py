from transformers import pipeline


class Summarizer:
    model_name = "sshleifer/distilbart-cnn-12-6"
    model_revision = "a4f8f3e"
    task = "summarization"
    summarizer_max_length = 150
    summarizer_min_length = 30

    def get_summarized_text(self, text_to_be_summarized):
        return self._get_summarized_text(text_to_be_summarized)

    def _get_summarized_text(self, text_to_be_summarized):
        # Use the summarization pipeline with the specified model
        summarizer = pipeline(self.task, model=self.model_name, revision=self.model_revision)

        # Generate the summary
        summary = summarizer(text_to_be_summarized, max_length=self.summarizer_max_length, min_length=self.summarizer_min_length, do_sample=False)

        # Extract the summarized text
        summarized_text = summary[0]['summary_text']

        return summarized_text
