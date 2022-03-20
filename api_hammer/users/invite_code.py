from string import ascii_letters
from random import randint, choice


def get_invite_code():
    return (
        f'{randint(0,10)}{choice(ascii_letters)}'+
        f'{randint(0,10)}{choice(ascii_letters)}'+
        f'{randint(0,10)}{choice(ascii_letters)}'
    )
