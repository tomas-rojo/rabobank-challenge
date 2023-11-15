# Word Frequency Analyzer
A Python class that analyze words and frequency in a text.

## Installation
Clone the repository
```
git clone https://github.com/tomas-rojo/rabobank-challenge.git
cd rabobank-challenge
```
### Regular installation
Create a virtual environment and install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Using Docker
With the use of make commands we can simply have an image ready to use for testing and execution.
1. **Build the image**
```
make build
```
2. **Run the tests inside the container**
```
make test_in_docker
```
3. **Run the application**
```
make start
```
## Usage

The class `WordFrequencyAnalyzer` contains 3 methods:
* `calculate_highest_frequency` returns the most frequent word in the text.
* `calculate_frequency_for_word` returns the frequency of the specified word.
* `calculate_most_frequent_n_words` returns a list with the most frequent n words in the text ordered alphabetically.

```python
sample_text = "The sun shines over the lake"
analyzer = WordFrequencyAnalyzer()

highest_frequency = analyzer.calculate_highest_frequency(sample_text)
# 2

frequency_for_word = analyzer.calculate_frequency_for_word(sample_text, "the")
# 2

most_frequent_n_words = analyzer.calculate_most_frequent_n_words(sample_text, 3)
# [('the', 2), ('lake', 1), ('over', 1)]
```
