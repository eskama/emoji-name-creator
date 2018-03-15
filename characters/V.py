"""
author: mertkosan
createdAt: 3/12/2018
"""
from random import choice
from emojis import emojis, empty_emoji


class V:
    def __init__(self):
        self.__v = ""

    def reset(self):
        self.__v = ""

    def first(self):
        first_str = choice(empty_emoji) + choice(emojis)
        for i in range(3):
            first_str += choice(empty_emoji)
        self.__v += first_str + choice(emojis) + choice(empty_emoji) + "\n"
        return first_str

    def second(self):
        return self.first()

    def third(self):
        return self.first()

    def fourth(self):
        return self.first()

    def fifth(self):
        fifth_str = choice(empty_emoji) + choice(empty_emoji) + \
                    choice(emojis) + \
                    choice(empty_emoji) + \
                    choice(emojis) + \
                    choice(empty_emoji) + choice(empty_emoji)
        self.__v += fifth_str + "\n"
        return fifth_str

    def sixth(self):
        return self.fifth()

    def seventh(self):
        seventh_str = ""
        for i in range(3):
            seventh_str += choice(empty_emoji)
        seventh_str += choice(emojis)
        for i in range(3):
            seventh_str += choice(empty_emoji)
        self.__v += str(seventh_str) + "\n"
        return seventh_str

    def create(self):
        self.reset()
        self.first()
        self.second()
        self.third()
        self.fourth()
        self.fifth()
        self.sixth()
        self.seventh()
        return self.__v
