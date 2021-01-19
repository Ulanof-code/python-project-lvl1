from brain_games.common_components.round_counter import count
from brain_games.common_components.greetings import welcome_user
from random import randint
import prompt


def start_prime_game():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while not count(counter):
        num = randint(0, 50)
        print(f"Question: {num}")
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_prime(num) else 'no'
        if answer == correct_answer:
            print('Correct!')
            counter = counter + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.Let's try again, {user_name}!")  # noqa E501
            return
    if count(counter):
        print(f'Congratularions, {user_name}!')



def is_prime(value):
    if value < 2 or value % 2 == 0:
        return False
    divider = 3
    while divider <= value // 2:
        if value % divider == 0:
            return False
        divider += 1
    return True
