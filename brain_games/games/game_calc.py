from brain_games.common_components.round_counter import count
from brain_games.common_components.greetings import welcome_user
from random import randint
import prompt


def start_calc_game():
    user_name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    while not count(counter):
        operation = randint(0, 2)  # 0 - multiply; 1 - addition; 2 - subtract
        if operation == 0:  # multiplication operation
            if multiplication_operation():
                counter = counter + 1
                continue
            else:
                print(f"Let's try again, {user_name}!")
                return

        if operation == 1:  # addition operation
            if addition_operation():
                counter = counter + 1
                continue
            else:
                print(f"Let's try again, {user_name}!")
                return

        if operation == 2:  # subtraction operation
            if subtraction_operation():
                counter = counter + 1
                continue
            else:
                print(f"Let's try again, {user_name}!")
                return
    if counter == 3:
        print(f"Congratulations, {user_name}!")


def multiplication_operation():
    a = str(randint(0, 25))
    b = str(randint(0, 25))
    print(f'Question: {a + " * " + b}')
    answer = prompt.string('Your answer: ')
    if int(answer) == (int(a) * int(b)):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{int(a)*int(b)}'")  # noqa: E501
        return False


def addition_operation():
    a = str(randint(0, 25))
    b = str(randint(0, 25))
    print(f'Question: {a + " + " + b}')
    answer = prompt.string('Your answer: ')
    if int(answer) == (int(a) + int(b)):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{int(a)+int(b)}'")  # noqa: E501
        return False


def subtraction_operation():
    a = str(randint(0, 25))
    b = str(randint(0, int(a)))
    print(f'Question: {a + " - " + b}')
    answer = prompt.string('Your answer: ')
    if int(answer) == (int(a) - int(b)):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{int(a) - int(b)}'")  # noqa: E501
        return False
