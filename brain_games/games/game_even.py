from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer_pair():
    """The function returns the value to start the game
     and the correct answer"""
    value = randint(0, 100)
    answer = 'yes' if is_even(value) else 'no'
    return value, answer


def is_even(value):
    """The function checks whether the value is even or odd.
     If the value is even,it is True,
     if it is odd, it is False."""
    return True if value % 2 == 0 else False
