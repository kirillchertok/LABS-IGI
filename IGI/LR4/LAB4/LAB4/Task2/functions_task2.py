# -*- coding: cp1251 -*-

import re
import zipfile

class TextAnalyzer:
    class_attribute = "TextAnalyzer"

    def __init__(self, filename):
        self.filename = filename
        self.text = self.read_text(filename)
        
    @staticmethod
    def static_method():
        return "This is static method"
    @classmethod
    def get_all(self):
        return (self.filename, self.text)
    @property
    def filename(self):
        return self.filename
    @property
    def text(self):
        return self.text
    @filename.setter
    def filename(self, value):
        self.filename = value
    @text.setter
    def text(self, value):
        self.text = value

    def read_text(self, filename):
        """
        Reads text from a file.

        :param filename: The name of the file to read.
        :return: Text from the file.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    def count_sentences(self):
        """
        Counts the number of sentences in the text.

        :return: The number of sentences.
        """
        return len(re.findall(r'[.!?]', self.text))

    def count_sentence_types(self):
        """
        Counts the number of sentences of each type: narrative, interrogative, and imperative.

        :return: A dictionary with counts of each sentence type.
        """
        narrative_count = len(re.findall(r'[.](?:\s+[A-Z])?', self.text))
        interrogative_count = len(re.findall(r'[?](?:\s+[A-Z])?', self.text))
        imperative_count = len(re.findall(r'[!](?:\s+[A-Z])?', self.text))
        return {
            'narrative_count': narrative_count,
            'interrogative_count': interrogative_count,
            'imperative_count': imperative_count
        }

    def calculate_average_sentence_length(self):
        """
        Calculates the average sentence length in characters.

        :return: The average sentence length.
        """
        sentence_lengths = [len(sentence) for sentence in re.split(r'[.!?]', self.text) if sentence.strip()]
        return sum(sentence_lengths) / len(sentence_lengths)

    def calculate_average_word_length(self):
        """
        Calculates the average word length in characters.

        :return: The average word length.
        """
        words = re.findall(r'\b\w+\b', self.text)
        return sum(len(word) for word in words) / len(words)

    def count_smileys(self):
        """
        Counts the number of smileys in the text.

        :return: The number of smileys.
        """
        return len(re.findall(r'[;:]-*[\(\[\]\)]+', self.text))

    def find_three_letter_words(self):
        """
        Finds all three-letter words in the text.

        :return: A list of three-letter words.
        """
        return [word for word in re.findall(r'\b\w{3}\b', self.text)]

    def find_words_with_equal_vowels_consonants(self):
        """
        Finds words with an equal number of vowels and consonants.

        :return: A list of words meeting the criteria.
        """
        vowels = 'aeiouyAEIOUY'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        return [word for word in re.findall(r'\b\w+\b', self.text) if sum(1 for char in word if char in vowels) == sum(1 for char in word if char in consonants)]

    def sort_words_by_length(self):
        """
        Sorts words in descending order of their lengths.

        :return: A list of words sorted by length.
        """
        return sorted(re.findall(r'\b\w+\b', self.text), key=len, reverse=True)

    def analyze_text(self):
        """
        Analyzes the text and returns the analysis results.

        :return: Analysis results of the text.
        """
        return {
            'sentence_count': self.count_sentences(),
            **self.count_sentence_types(),
            'average_sentence_length': self.calculate_average_sentence_length(),
            'average_word_length': self.calculate_average_word_length(),
            'smiley_count': self.count_smileys(),
            'three_letter_words': self.find_three_letter_words(),
            'equal_vowels_consonants': self.find_words_with_equal_vowels_consonants(),
            'words_sorted_by_length': self.sort_words_by_length()
        }

    def replace_spaces(self, replacement):
        """
        Replaces spaces in the text with the specified symbol.

        :param replacement: The symbol to replace spaces.
        :return: Text with replaced spaces.
        """
        return self.text.replace(' ', replacement)

    def is_guid_with_brackets(self, text):
        """
        Checks if the given string is a GUID with brackets.

        :param text: The string to check.
        :return: True if the string is a GUID with brackets, False otherwise.
        """
        return re.match(r'\{?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\}?', text) is not None

    def save_results_to_file(self, filename, results):
        """
        Saves the analysis results to a file.

        :param filename: The name of the file to save results.
        :param results: The analysis results.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for key, value in results.items():
                file.write(f"{key}: {value}\n")

    def zip_results_file(self, filename, zip_filename):
        """
        Archives the results file using the zipfile module.

        :param filename: The name of the file to archive.
        :param zip_filename: The name of the zip file.
        """
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(filename)
            
    def zip_file_unpack(self, zip_filename):
        """
        Archives the results file using the zipfile module.

        :param zip_filename: The name of the zip file.
        """
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            file_list = zipf.namelist()
            for file in file_list:
                zipf.extract(file)

    def print_results(self, results):
        """
        Prints the analysis results to the screen.

        :param results: The analysis results.
        """
        print("\nРезультаты анализа текста:")
        for key, value in results.items():
            print(f"{key}: {value}")
    