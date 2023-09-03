import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

from loguru import logger

from base.summarizer import Summarizer


class ExtractiveSummarizer(Summarizer):
    """
    Concrete summarizer using nltk
    """

    def __init__(self):
        self._max_length_of_summary = 450

    def _create_frequency_table(self, text_string):
        stop_words = set(stopwords.words("english"))
        words = word_tokenize(text_string)
        ps = PorterStemmer()

        freq_table = dict()
        for word in words:
            word = ps.stem(word)
            if word in stop_words:
                continue
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
        return freq_table

    def _filter_out_duplicate_sentences(self, sentences):
        processed_sentences = set()
        non_duplicate_sentences = []
        for sentence in sentences:
            if sentence.lower() in processed_sentences:
                continue
            non_duplicate_sentences.append(sentence)
            processed_sentences.add(sentence.lower())
        return non_duplicate_sentences

    def _score_sentences(self, sentences, freq_table):
        sentence_value = dict()
        for sentence in sentences:
            word_count_in_sentence = (len(word_tokenize(sentence)))
            for word_value in freq_table:
                if word_value in sentence.lower():
                    if sentence[:10] in sentence_value:
                        sentence_value[sentence[:10]] += freq_table[word_value]
                    else:
                        sentence_value[sentence[:10]] = freq_table[word_value]

            sentence_value[sentence[:10]] = sentence_value[sentence[:10]] // word_count_in_sentence
        return sentence_value

    def _find_average_score(self, sentence_value):
        sum_values = 0
        for entry in sentence_value:
            sum_values += sentence_value[entry]
        average = int(sum_values / len(sentence_value))
        return average

    def _generate_summary(self, sentences, sentence_value, threshold, max_length_of_summary):
        summary = ''
        for sentence in sentences:
            if max_length_of_summary and len(summary) >= max_length_of_summary:
                break
            if sentence[:10] in sentence_value and sentence_value[sentence[:10]] >= threshold:
                summary += " " + sentence
        return summary

    def get_summarized_text(self, text_to_be_summarized, max_length=None):

        # 0 Cleaning the data
        logger.info("Cleaning the data")
        text_to_be_summarized = re.sub(r"[^a-zA-Z0-9\s.,]", "", text_to_be_summarized)

        # 1 Create the word frequency table
        logger.info("Creating frequency table")
        freq_table = self._create_frequency_table(text_to_be_summarized)

        # 2 Tokenize the sentences
        logger.info("Tokenizing sentences")
        sentences = sent_tokenize(text_to_be_summarized)

        # 3 Filter out duplicate sentences
        logger.info("Filtering out duplicate sentences")
        sentences = self._filter_out_duplicate_sentences(sentences)

        # 4 Score the sentences
        logger.info("Scoring sentences")
        sentence_scores = self._score_sentences(sentences, freq_table)

        # 5 Find the threshold
        logger.info("Finding the threshold")
        threshold = self._find_average_score(sentence_scores)

        # 6 Generate the summary
        logger.info("Generating summary")
        if max_length is None:
            max_length_of_summary = None
        else:
            # Sorting sentence scores to restrict maximum length of summary
            sentence_scores = dict(sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True))
            max_length_of_summary = max_length

        summary = self._generate_summary(sentences, sentence_scores, threshold, max_length_of_summary=max_length_of_summary)
        logger.info("Summary is ready to be picked up")

        return summary.lstrip().rstrip()
