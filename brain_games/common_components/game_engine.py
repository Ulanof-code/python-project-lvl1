from brain_games.common_components.round_counter import count
from brain_games.common_components.greetings import welcome_user
from prompt import string


def start(game):
    user_name = welcome_user()
    print(game.GAME_DESCRIPTION)
    counter = 0
    while not count(counter):
        value, result = game.set_value_and_result()
        print(f'Question: {value}')
        answer = string('Your answer: ')
        if answer == result:
            print('Correct!')
            counter += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  "Let's try again, '{}'"
                  .format(answer, result, user_name))
            return
    if count(counter):
        print('Congratulations, {}'.format(user_name))
