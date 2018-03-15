"""
author: mertkosan
createdAt: 3/15/2018
"""
from random import choice
from emojis import emojis, empty_emoji


class I:
    def __init__(self):
        self.__i = ""

    def reset(self):
        self.__i = ""

    def first(self):
        first_str = choice(empty_emoji) + choice(empty_emoji)
        for i in range(3):
            first_str += choice(emojis)
        self.__i += first_str + choice(empty_emoji) + choice(empty_emoji) + "\n"
        return first_str

    def second(self):
        return self.first()

    def third(self):
        third_str = ""
        for i in range(7):
            third_str += choice(empty_emoji)
        self.__i += third_str + "\n"
        return third_str

    def fourth(self):
        fourth_str = ""
        for i in range(3):
            fourth_str += choice(empty_emoji)
        fourth_str += choice(emojis)
        for i in range(3):
            fourth_str += choice(empty_emoji)
        self.__i += fourth_str + "\n"
        return fourth_str

    def fifth(self):
        return self.fourth()

    def sixth(self):
        return self.fourth()

    def seventh(self):
        return self.fourth()

    def create(self):
        self.reset()
        self.first()
        self.second()
        self.third()
        self.fourth()
        self.fifth()
        self.sixth()
        self.seventh()
        return self.__i
