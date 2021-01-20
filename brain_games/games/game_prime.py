from random import randint

GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def set_value_and_result():
    """The function sets the values and returns the correct result"""
    value = randint(1, 3571)
    result = 'yes' if get_result(value) else 'no'
    return value, result


def get_result(value):
    """The function checks if the number is prime.
    The function returns True if the number is prime,
    otherwise it returns False"""
    if value < 2 or value % 2 == 0:
        return False
    divisor = 3
    while divisor <= value // 2:
        if value % divisor == 0:
            return False
        divisor += 1
    return True
