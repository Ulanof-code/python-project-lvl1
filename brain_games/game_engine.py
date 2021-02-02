from brain_games.greetings import welcome_user
from prompt import string

ROUNDS_COUNT = 3


def start(game):
    user_name = welcome_user()
    print(game.GAME_DESCRIPTION)
    current_round = 0
    while current_round < ROUNDS_COUNT:
        question, correct_answer = game.generate_question_answer()
        print(f'Question: {question}')
        player_answer = string('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
            current_round += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  "Let's try again, {}!"
                  .format(player_answer, correct_answer, user_name))
            return
    else:
        print('Congratulations, {}!'.format(user_name))
