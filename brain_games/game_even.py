import prompt
from random import randint


def start_even_game():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_number = randint(1, 10000)
        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            if answer == 'yes':
                counter = counter + 1
                print('Correct!')
            else:
                counter = 0
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again, {}!".format(name))
                continue
        elif random_number % 2 == 1:
            if answer == 'no':
                counter = counter + 1
                print('Correct!')
            else:
                counter = 0
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, {}!".format(name))
                continue
        if counter == 3:
            print('Congratulations, {}!'.format(name))