# -*- coding: UTF-8 -*-
import os

emojis = [
    {
        'empty': ['👸', '🤴', '🕵‍♂', '🕵‍♀', '😊', '🤖', '👻', '🍫', '☕', '🍩', '⚽', '🎱', '😍', '👽', '🎻', '🧘‍♀', '🧘‍♂'],
        'pattern': ['🔥']
    },
    {
        'empty': ['⬜'],
        'pattern': ['👸', '🤴', '🕵‍♂', '🕵‍♀', '😊', '🤖', '👻', '🍫', '☕', '🍩', '⚽', '🎱', '😍', '👽', '🎻', '🧘‍♀', '🧘‍♂']
    },
    {
        'empty': ['⬜'],
        'pattern': ['🔥']
    }
]
size = {
    'SMALL': {
        'name': 'small',
        'width': 3,
        'height': 5
    },
    'MEDIUM': {
        'name': 'medium',
        'width': 5,
        'height': 7
    }
}
GENERATOR_DIR = os.path.dirname(os.path.abspath(__file__))
