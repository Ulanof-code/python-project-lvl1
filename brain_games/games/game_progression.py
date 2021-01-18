from brain_games.common_components.round_counter import count
from brain_games.common_components.greetings import welcome_user
from random import randint
import prompt


def start_progression_game():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    counter = 0
    while not count(counter):
        step = randint(2, 5)
        final_value = randint(step * 10, 50)
        starting_value = randint(0, (final_value - (step * 10)))
        secret_numb = randint(0, len(build_list(starting_value, final_value, step)) - 1)
        correct_answer = build_list(starting_value, final_value, step)[secret_numb]
        print("Question: " + build_progression(build_list(starting_value, final_value, step), secret_numb))
        answer = prompt.string('Your answer: ')
        if correct_answer == int(answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.Let's try again, {user_name}!")
            return
    if count(counter):
        print(f'Congratularions, {user_name}!')


def build_list(starting_value, final_value, step):
    return list(range(starting_value, final_value, step))


def build_progression(list_progression, secret_numb):
    line_numb = ""
    for i in range(len(list_progression)):
        if i == secret_numb:
            list_progression[i] = ".."
        line_numb = line_numb + str(list_progression[i]) + " "
    return line_numb
