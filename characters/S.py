"""
author: mertkosan
createdAt: 3/12/2018
"""
from random import choice
from emojis import emojis, empty_emoji


class S:
    def __init__(self):
        self.__s = ""

    def reset(self):
        self.__s = ""

    def first(self):
        first_str = choice(empty_emoji)
        for i in range(5):
            first_str += choice(emojis)
        self.__s += first_str + choice(empty_emoji) + "\n"
        return first_str

    def second(self):
        second_str = choice(empty_emoji) + choice(emojis)
        for i in range(4):
            second_str += choice(empty_emoji)
        self.__s += second_str + choice(empty_emoji) + "\n"
        return second_str

    def third(self):
        return self.second()

    def fourth(self):
        return self.first()

    def fifth(self):
        fifth_str = choice(empty_emoji)
        for i in range(4):
            fifth_str += choice(empty_emoji)
        fifth_str += choice(emojis)
        self.__s += fifth_str + choice(empty_emoji) + "\n"
        return fifth_str

    def sixth(self):
        return self.fifth()

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
        return self.__s
