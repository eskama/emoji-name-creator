from pattern.generator import SequenceGenerator

if __name__ == '__main__':
    # TODO: get these options as input
    pattern = 'sevgi'
    pattern_option = 'letter'
    style = 1
    size = 'medium'
    direction = 'vertical'
    framed = True
    print_file = True
    result_file_name = 'result/' + "_".join([pattern, pattern_option, str(style), size, direction, str(framed)])

    result = SequenceGenerator(sequence=pattern, option=pattern_option, style=style,
                               size=size, direction=direction, framed=framed).generate()

    print result

    if print_file:
        with open(result_file_name, 'w') as __pattern_file:
            __pattern_file.write(result)
