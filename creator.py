from pattern.generator import EmojiGenerator
from pattern import settings

if __name__ == '__main__':
    # TODO: get these options as input
    pattern = 'sevgi'
    pattern_option = 'letter'
    style = 1
    size = 'medium'
    print_file = True
    result = ""

    if pattern_option == 'letter':
        for ch in pattern:
            result += EmojiGenerator(pattern=ch, pattern_option=pattern_option, pattern_style=style, size=size) \
                .create(up=True, left=True, right=True)
        result += EmojiGenerator(pattern=pattern, pattern_option=pattern_option, pattern_style=style, size=size)\
            .horizontal_line(settings.size[size]['width'] + 2)

    print result

    if print_file:
        with open('result/' + pattern, 'w') as __pattern_file:
            __pattern_file.write(result)
