

class Letter(object):

    def __init__(self, char):
        print('new letter "{}" created'.format(char))
        self._char = char

    def get_value(self):
        return self._char


class LetterSimpleFactory(object):
    _letters = dict()

    @classmethod
    def instance(cls, char):
        if char not in cls._letters:
            letter = Letter(char)
            cls._letters[char] = letter
        return cls._letters[char]
