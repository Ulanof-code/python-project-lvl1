from random import randint, choice
from operator import add, sub, mul

GAME_DESCRIPTION = 'What is the result of the expression?'
ARITHMETIC_OPERATIONS = ['+', '-', '*']


def generate_question_answer():
    """The function sets and returns an expression and a calculated result"""
    arithmetic_operation = choice(ARITHMETIC_OPERATIONS)
    value1, value2 = randint(0, 25), randint(0, 25)
    return (
        '{} {} {}'.format(value1, arithmetic_operation, value2),
        str(calc(arithmetic_operation, value1, value2))
    )


def calc(arithmetic_operation, value1, value2):
    if arithmetic_operation == '+':
        return add(value1, value2)
    elif arithmetic_operation == '-':
        return sub(value1, value2)
    elif arithmetic_operation == '*':
        return mul(value1, value2)
