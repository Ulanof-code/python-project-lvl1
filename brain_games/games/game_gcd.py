from brain_games.common_components.round_counter import count
from brain_games.common_components.greetings import welcome_user
from random import randint
import prompt


def start_gcd_game():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    counter = 0
    while not count(counter):
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        print("Question: {}".format(str(number1) + " " + str(number2)))
        answer = prompt.string("Your answer: ")
        if int(answer) == calculate_gcd(number1, number2):
            print("Correct!")
            counter = counter + 1
        else:
            print("{} is wrong answer ;(. Correct answer was '{}'".format(answer, str(calculate_gcd(number1, number2))))
            print(f"Let's try again, {user_name}!")
            return
    if count(counter):
        print(f"Congratulations, {user_name}!")


def calculate_gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1
