from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def set_value_and_result():
    """The function returns the value to start the game
     and the correct answer"""
    value = randint(0, 100)
    result = 'yes' if get_result(value) else 'no'
    return value, result


def get_result(value):
    """The function checks whether the value is even or odd.
     If the value is even,it is True,
     if it is odd, it is False."""
    return True if value % 2 == 0 else False
