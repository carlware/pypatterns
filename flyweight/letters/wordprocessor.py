from __future__ import print_function


class WordProcessor(object):

    def __init__(self):
        self.letters = []

    def add_letter(self, letter):
        self.letters.append(letter)

    def print_letters(self):
        for letter in self.letters:
            print(letter.get_value(), end='')
        print("")
