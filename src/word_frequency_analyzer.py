from collections import Counter
from dataclasses import astuple, dataclass
from typing import List, Tuple
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class WordFrequency:
    word: str
    frequency: int


class WordFrequencyAnalyzer:
    @staticmethod
    def calculate_highest_frequency(text: str) -> int:
        """
        Calculates the highest frequency of words in the input text.
        """
        word_counts = WordFrequencyAnalyzer._count_words(text)
        return max(word_counts.values()) if word_counts else 0

    @staticmethod
    def calculate_frequency_for_word(text: str, word: str) -> int:
        """
        Calculates the frequency of a specific word in the input text.
        """
        word_counts = WordFrequencyAnalyzer._count_words(text)
        return word_counts.get(word.lower(), 0)

    @staticmethod
    def calculate_most_frequent_n_words(
        text: str, n: int
    ) -> List[Tuple[WordFrequency]]:
        """
        Calculates the most frequent 'n' words in the input text.
        """
        word_counts = WordFrequencyAnalyzer._count_words(text)
        sorted_word_counts = sorted(
            word_counts.items(), key=lambda x: (-x[1], x[0].lower())
        )
        most_frequent_n_words = sorted_word_counts[:n]
        return [
            astuple(WordFrequency(word, frequency))
            for word, frequency in most_frequent_n_words
        ]

    @staticmethod
    def _count_words(text: str) -> Counter[str]:
        """
        Counts the frequency of words in the input text.
        """
        words = text.lower().split()
        words_counter = Counter(words)
        return words_counter


if __name__ == "__main__":
    sample_text = "The sun shines over the lake"

    analyzer = WordFrequencyAnalyzer()
    word_to_find = "the"
    n_words = 3

    highest_frequency = analyzer.calculate_highest_frequency(sample_text)
    logging.info("Highest frequency: %d", highest_frequency)

    frequency_for_word = analyzer.calculate_frequency_for_word(
        sample_text, word_to_find
    )
    logging.info("Frequency for %s: %d", word_to_find, frequency_for_word)

    most_frequent_n_words = analyzer.calculate_most_frequent_n_words(
        sample_text, n_words
    )
    logging.info("Most frequent words: %s", most_frequent_n_words)
