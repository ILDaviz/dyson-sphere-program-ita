""" Files map """

import os

def get_files():
    """ Get files """

    if os.getenv('DEV_MODE'):
        files = [
            'demo.txt',
        ]
    else:
        files = [
            '[outsource].txt',
            '[user].txt',
            'combat.txt',
            'creation.txt',
            'dictionary.txt',
            'prototype.txt',
            'base.txt'
        ]

    return files
