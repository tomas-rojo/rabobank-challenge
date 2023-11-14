from pytest import fixture

from word_frequency_analyzer import WordFrequency, WordFrequencyAnalyzer


@fixture
def analyzer() -> WordFrequencyAnalyzer:
    return WordFrequencyAnalyzer()


def test_can_instantiate_word_frequency():
    word = WordFrequency(word="a", frequency=1)
    assert word.word == "a"
    assert word.frequency == 1

def test_calculate_highest_frequency(analyzer: WordFrequencyAnalyzer) -> None:
    text = "The sun shines over the lake"
    assert analyzer.calculate_highest_frequency(text) == 2


def test_calculate_highest_frequency_with_empty_text(
    analyzer: WordFrequencyAnalyzer,
) -> None:
    assert analyzer.calculate_highest_frequency("") == 0


def test_calculate_highest_frequency_with_single_word(
    analyzer: WordFrequencyAnalyzer,
) -> None:
    assert (
        analyzer.calculate_highest_frequency(
            "In this sentence there are only single words"
        )
        == 1
    )


def test_calculate_highest_frequency_with_duplicate_words(
    analyzer: WordFrequencyAnalyzer,
) -> None:
    assert (
        analyzer.calculate_highest_frequency(
            "My name is Tomas Rojo, toMas is software developer, tomaS likes Python"
        )
        == 3
    )


def test_calculate_frequency_for_word(analyzer: WordFrequencyAnalyzer) -> None:
    text = "The sun shines over thE lake"
    assert analyzer.calculate_frequency_for_word(text, "the") == 2
    assert analyzer.calculate_frequency_for_word(text, "lake") == 1


def test_calculate_most_frequent_n_words(analyzer: WordFrequencyAnalyzer) -> None:
    input_text = "C b A e D a Z"
    result = analyzer.calculate_most_frequent_n_words(input_text, 3)
    expected_result = [("a", 2), ("b", 1), ("c", 1)]
    assert result == expected_result


def test_calculate_most_frequent_n_words_with_empty_text(
    analyzer: WordFrequencyAnalyzer,
) -> None:
    assert analyzer.calculate_most_frequent_n_words("", 3) == []


def test_calculate_most_frequent_n_words_with_single_word(
    analyzer: WordFrequencyAnalyzer,
) -> None:
    assert analyzer.calculate_most_frequent_n_words("word", 1) == [("word", 1)]


def test_calculate_most_frequent_n_words_with_mixed_case(
    analyzer: WordFrequencyAnalyzer,
) -> None:
    input_text = "tHe sUn ShInEs oVeR tHe LaKe"
    result = analyzer.calculate_most_frequent_n_words(input_text, 3)
    assert result == [("the", 2), ("lake", 1), ("over", 1)]
