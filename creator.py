from characters import S, E, V, G, I
from operator import methodcaller
from emojis import empty_emoji
from random import choice

class_dict = {
    'S': S.S(),
    'E': E.E(),
    'V': V.V(),
    'G': G.G(),
    'I': I.I()
}

functions = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']


def create_horizontal(name):
    classes = []
    for ch in name:
        classes.append(class_dict[ch.upper()])

    result = ""

    for k in range(len(classes)):
        for m in range(6):
            result += choice(empty_emoji)
    result += choice(empty_emoji) + "\n"

    for i in range(7):
        result += choice(empty_emoji)
        for j in range(len(classes)):
            f = methodcaller(functions[i])
            result += f(classes[j])
            result += "" if (j + 1) is len(classes) else choice(empty_emoji)
        result += choice(empty_emoji)
        result += "\n"

    for k in range(len(classes)):
        for s in range(6):
            result += choice(empty_emoji)
    result += choice(empty_emoji) + "\n"

    return result


def create_vertical(name):
    classes = []
    for ch in name:
        classes.append(class_dict[ch.upper()])
    result = ""
    for i in range(len(classes)):
        for j in range(7):
            result += choice(empty_emoji)
        result += '\n'
        result += classes[i].create()
    for k in range(7):
        result += choice(empty_emoji)
    result += '\n'
    return result


name = 'sevgi'

result_se = create_vertical(name)

file = open('results/' + name, 'w')
file.write(result_se)
file.close()
