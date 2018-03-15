"""
author: mertkosan
createdAt: 3/12/2018
"""
from random import choice
from emojis import emojis, empty_emoji


class G:
    def __init__(self):
        self.__g = ""

    def reset(self):
        self.__g = ""

    def first(self):
        first_str = choice(empty_emoji)
        for i in range(5):
            first_str += choice(emojis)
        self.__g += first_str + choice(empty_emoji) + "\n"
        return first_str

    def second(self):
        second_str = choice(empty_emoji) + choice(emojis)
        for i in range(4):
            second_str += choice(empty_emoji)
        self.__g += second_str + choice(empty_emoji) + "\n"
        return second_str

    def third(self):
        return self.second()

    def fourth(self):
        fourth_str = choice(empty_emoji) + choice(emojis) + choice(empty_emoji)
        for i in range(3):
            fourth_str += choice(emojis)
        self.__g += fourth_str + choice(empty_emoji) + "\n"
        return fourth_str

    def fifth(self):
        fourth_str = choice(empty_emoji) + choice(emojis)
        for i in range(3):
            fourth_str += choice(empty_emoji)
        self.__g += fourth_str + choice(emojis) + choice(empty_emoji) + "\n"
        return fourth_str

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
        return self.__g
