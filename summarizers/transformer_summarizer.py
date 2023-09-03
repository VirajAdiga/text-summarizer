from transformers import BartTokenizer, BartForConditionalGeneration

from loguru import logger

from base.summarizer import Summarizer


class TransformersSummarizer(Summarizer):
    """
    Concrete summarizer using transformers
    """

    def _initialize_model(self):
        model_name = 'facebook/bart-large-cnn'
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def get_summarized_text(self, text_to_be_summarized, max_length=None):

        # Initialize model
        logger.info(f"Initializing the transformer model")
        self._initialize_model()

        inp = self.tokenizer.encode(text_to_be_summarized, return_tensors='pt', max_length=1024)

        # Generate summary
        logger.info(f"Generating summary")
        if max_length is None:
            summary_ids = self.model.generate(inp, num_beams=4, early_stopping=True)
        else:
            summary_ids = self.model.generate(inp, num_beams=4, max_length=max_length, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        logger.info(f"Summary is ready to be picked up")
        return summary.lstrip().rstrip()
