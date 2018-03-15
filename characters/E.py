"""
author: mertkosan
createdAt: 3/12/2018
"""
from random import choice
from emojis import emojis, empty_emoji


class E:
    def __init__(self):
        self.__e = ""

    def reset(self):
        self.__e = ""

    def first(self):
        first_str = choice(empty_emoji)
        for i in range(5):
            first_str += choice(emojis)
        self.__e += first_str + choice(empty_emoji) + "\n"
        return first_str

    def second(self):
        second_str = choice(empty_emoji) + choice(emojis)
        for i in range(4):
            second_str += choice(empty_emoji)
        self.__e += second_str + choice(empty_emoji) + "\n"
        return second_str

    def third(self):
        return self.second()

    def fourth(self):
        return self.first()

    def fifth(self):
        return self.second()

    def sixth(self):
        return self.second()

    def seventh(self):
        return self.first()

    def create(self):
        self.reset()
        self.first()
        self.second()
        self.third()
        self.fourth()
        self.fifth()
        self.sixth()
        self.seventh()
        return self.__e
