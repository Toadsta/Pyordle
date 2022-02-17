import random
from word_getter import data
from word_size_getter import list_by_size

class Pyordle:
    def __init__(self, lives, word):
        self.lives = lives
        self.word = word
