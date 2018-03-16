from random import choice
import settings


class EmojiGenerator:
    def __init__(self, pattern, pattern_option='letter', pattern_style=1, size='medium'):
        self.__pattern = pattern.upper()
        self.__pattern_option = pattern_option
        self.__style = settings.emojis[pattern_style]
        self.__size = settings.size[size]

    def create(self, up=False, down=False, left=False, right=False):
        """
        create pattern and return
        :param up: put empty emojis up of pattern
        :param down: put empty emojis down of pattern
        :param left: put empty emojis left of pattern
        :param right: put empty emojis right of pattern
        :return: pattern
        """
        __result = ""
        with open(settings.GENERATOR_DIR + '/' + self.__size['name'] + '/' + self.__pattern_option + '/' + self.__pattern) as __file:
            lines = __file.readlines()
            if up:
                __result += choice(self.__style['empty']) if left else ""
                __result += self.horizontal_line(self.__size['width'])
                __result += choice(self.__style['empty']) if right else ""
                __result += '\n'
            for line in lines:
                line = line.strip()
                __result += choice(self.__style['empty']) if left else ""
                for ch in line:
                    __result += choice(self.__style['empty']) if ch == 'O' else choice(self.__style['pattern'])
                __result += choice(self.__style['empty']) if right else ""
                __result += '\n'
            if down:
                __result += choice(self.__style['empty']) if left else ""
                __result += self.horizontal_line(self.__size['width'])
                __result += choice(self.__style['empty']) if right else ""
                __result += '\n'
        return __result

    def horizontal_line(self, number):
        """
        :param number: how many emojis line will consist
        :return: horizontal line with empty emojis
        """
        __line = ""
        for i in range(number):
            __line += choice(self.__style['empty'])
        return __line
