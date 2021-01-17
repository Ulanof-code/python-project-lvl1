import prompt
from random import randint
from brain_games.common_components.greetings import welcome_user


def start_even_game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = randint(1, 10000)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            if answer == 'yes':
                counter = counter + 1
                print('Correct!')
            else:
                counter = 0
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {user_name}!")
                continue
        elif random_number % 2 == 1:
            if answer == 'no':
                counter = counter + 1
                print('Correct!')
            else:
                counter = 0
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {user_name}!")
                continue
        if counter == 3:
            print(f'Congratulations, {user_name}!')
