from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def set_value_and_result():
    """The function sets the values and returns the correct result"""
    value1, value2 = randint(1, 100), randint(1, 100)
    return (
        '{} {}'.format(value1, value2),
        str(get_result(value1, value2)),
    )


def get_result(value1, value2):
    """The function calculates the greatest common divisor and returns the result"""
    while value1 != value2:
        if value1 > value2:
            value1 = value1 - value2
        else:
            value2 = value2 - value1
    return value1
