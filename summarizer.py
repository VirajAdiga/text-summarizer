import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

from loguru import logger


class Summarizer:

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

    def _generate_summary(self, sentences, sentence_value, threshold):
        summary = ''
        for sentence in sentences:
            if sentence[:10] in sentence_value and sentence_value[sentence[:10]] > threshold:
                summary += " " + sentence
        return summary

    def _get_summarized_text(self, text_to_be_summarized):

        # 0 Cleaning the data
        logger.info("Cleaning the data")
        text_to_be_summarized = re.sub(r"[^a-zA-Z0-9\s.,]", "", text_to_be_summarized)

        # 1 Create the word frequency table
        logger.info("Creating frequency table")
        freq_table = self._create_frequency_table(text_to_be_summarized)

        # 2 Tokenize the sentences
        logger.info("Tokenizing sentences")
        sentences = sent_tokenize(text_to_be_summarized)

        # 3 Score the sentences
        logger.info("Scoring sentences")
        sentence_scores = self._score_sentences(sentences, freq_table)

        # 4 Find the threshold
        logger.info("Finding the threshold")
        threshold = self._find_average_score(sentence_scores)

        # 5 Generate the summary
        logger.info("Generating summary")
        summary = self._generate_summary(sentences, sentence_scores, threshold)
        logger.info("Summary is ready to be picked up")

        return summary.lstrip().rstrip()

    def get_summarized_text(self, text_to_be_summarized):
        return self._get_summarized_text(text_to_be_summarized)
