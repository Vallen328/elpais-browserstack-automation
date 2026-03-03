import re
from collections import Counter


class TextAnalyzer:

    def __init__(self):
        # Common stop words to ignore
        self.stop_words = {
            "the", "and", "of", "in", "on", "a",
            "to", "for", "with", "one"
        }

    def analyze_word_frequency(self, texts, min_occurrences=3):
        """
        Count word frequency across list of strings.
        Returns words appearing >= min_occurrences.
        """

        all_words = []

        for text in texts:
            # Remove punctuation and lowercase
            cleaned_text = re.sub(r"[^\w\s]", "", text.lower())
            words = cleaned_text.split()

            filtered_words = [
                word for word in words
                if word not in self.stop_words
            ]

            all_words.extend(filtered_words)

        counter = Counter(all_words)

        frequent_words = {
            word: count
            for word, count in counter.items()
            if count >= min_occurrences
        }

        return frequent_words