from .wordprocessor import WordProcessor
from .factory import LetterSimpleFactory


class Client(object):

    def __init__(self, text):
        self.word_processor = WordProcessor()
        self.text = text
        self.add_letters()

    def add_letters(self):
        for c in self.text:
            letter = LetterSimpleFactory.instance(c)
            self.word_processor.add_letter(letter)

    def print_text(self):
        self.word_processor.print_letters()
