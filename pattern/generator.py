from random import choice
import settings
import utils


class SequenceGenerator:
    def __init__(self, sequence, option='letter', style=1, size='medium', direction='vertical', framed=True):
        self.__pattern = sequence.upper()
        self.__option = option.upper()
        self.__style = settings.emojis[style]
        self.__size = settings.size[size.upper()]
        self.__direction = direction.upper()
        self.__framed = framed

    def generate(self):
        result_pattern = ""
        if self.__option == 'LETTER':
            up, down, left, right = (True, True, True, True) if self.__framed else (False, False, False, False)
            if self.__direction == 'VERTICAL':
                for i, ch in enumerate(self.__pattern):
                    up = True if i == 0 and self.__framed else False
                    result_pattern += PatternGenerator(ch, self.__option, self.__style, self.__size)\
                        .generate(up, down, left, right)
            elif self.__direction == 'HORIZONTAL':
                for i, ch in enumerate(self.__pattern):
                    left = True if i == 0 and self.__framed else False
                    result_pattern = utils.concat(result_pattern,
                                                  PatternGenerator(ch, self.__option, self.__style, self.__size)
                                                  .generate(up, down, left, right))
            else:
                raise NotImplementedError('Direction only has vertical and horizontal options')
        else:
            raise NotImplementedError('Only letter option is available, right now')

        return result_pattern


class PatternGenerator:
    def __init__(self, pattern, option, style, size):
        self.__pattern = pattern.upper()
        self.__option = option
        self.__style = style
        self.__size = size
        self.__pattern_filename = settings.GENERATOR_DIR + '/' + self.__size['name'] + '/' + \
                                  self.__option + '/' + self.__pattern

    def generate(self, up=False, down=False, left=False, right=False):
        """
        create pattern and return
        :param up: put empty emojis up of pattern
        :param down: put empty emojis down of pattern
        :param left: put empty emojis left of pattern
        :param right: put empty emojis right of pattern
        :return: pattern
        """
        __result = ""
        with open(self.__pattern_filename) as __file:
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
