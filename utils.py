def concat(left, right):
    """
    concat two string horizontally line by line, length of line should be equal.
    :param left:
    :param right:
    :return:
    """
    if left == "":
        return right

    if right == "":
        return left

    result = ""
    left_lines = left.strip().split('\n')
    right_lines = right.strip().split('\n')
    if len(left_lines) == len(right_lines):
        for i in range(len(right_lines)):
            result += str(left_lines[i]) + str(right_lines[i]) + '\n'
        return result
    else:
        raise Exception('Left and Right string should have same length of lines.')
