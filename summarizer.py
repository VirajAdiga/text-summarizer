from transformers import T5ForConditionalGeneration, T5Tokenizer
from loguru import logger


class Summarizer:
    def get_summarized_text(self, text_to_be_summarized):
        return self._get_summarized_text(text_to_be_summarized)

    def _get_summarized_text(self, text_to_be_summarized):
        # Use the summarization pipeline with the specified model
        logger.info("Setting up the pipeline to summarize the text")

        model = T5ForConditionalGeneration.from_pretrained("t5-base")

        # initialize the model tokenizer
        tokenizer = T5Tokenizer.from_pretrained("t5-base")

        # encode the text into tensor of integers using the appropriate tokenizer
        inputs = tokenizer.encode("summarize: " + text_to_be_summarized, return_tensors="pt", max_length=512, truncation=True)

        # generate the summarization output
        logger.info("Generating the summary")
        outputs = model.generate(
            inputs,
            max_length=len(text_to_be_summarized)//8,
            min_length=len(text_to_be_summarized)//16,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True)
        logger.info("Summary is ready to be picked up")
        return tokenizer.decode(outputs[0])
