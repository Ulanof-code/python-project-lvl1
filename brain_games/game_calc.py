from brain_games.cli import welcome_user
from random import randint
import prompt


def start_calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        operation = randint(0, 2)  # 0 - multiplic; 1 - addit; 2 - subtract
        if operation == 0:  # multiplication operation
            if multiplication_operation():
                counter = counter + 1
                continue
            else:
                counter = 0
                print("Let's try again, {}!".format(name))
                continue

        if operation == 1:  # addition operation
            if addition_operation():
                counter = counter + 1
                continue
            else:
                counter = 0
                print("Let's try again, {}!".format(name))
                continue

        if operation == 2:  # subtraction operation
            if subtraction_operation():
                counter = counter + 1
                continue
            else:
                counter = 0
                print("Let's try again, {}!".format(name))
                continue
    if counter == 3:
        print("Congratulations, {}!".format(name))


def multiplication_operation():
    a = str(randint(0, 25))
    b = str(randint(0, 25))
    print('Question: {}'.format(a + ' * ' + b))
    answer = prompt.string('Your answer: ')
    if int(answer) == (int(a) * int(b)):
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answer, (int(a) * int(b))))  # noqa: E501
        return False


def addition_operation():
    a = str(randint(0, 25))
    b = str(randint(0, 25))
    print('Question: {}'.format(a + ' + ' + b))
    answer = prompt.string('Your answer: ')
    if int(answer) == (int(a) + int(b)):
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answer, (int(a) + int(b))))  # noqa: E501
        print("Let's try again, Sam!")
        return False


def subtraction_operation():
    a = str(randint(0, 25))
    b = str(randint(0, int(a)))
    print('Question: {}'.format(a + ' - ' + b))
    answer = prompt.string('Your answer: ')
    if int(answer) == (int(a) - int(b)):
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'".format(answer, (int(a) - int(b))))  # noqa: E501
        print("Let's try again, Sam!")
        return False
