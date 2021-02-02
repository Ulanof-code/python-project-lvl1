from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_question_answer():
    """
    The step variable is the step of the progression;
    The final_step variable is the final value of the whole progression;
    The variable start_value takes the initial value in the progression;
    The secret_numb variable is the index of the hidden number
    Function returns a finished arithmetic progression with the correct answer.
    """
    step = randint(2, 5)
    final_value = randint(step * 10, 50)
    start_value = randint(0, (final_value - (step * 10)))
    secret_numb = randint(0, len(range(start_value, final_value, step)) - 1)
    progression = build_progression(start_value, final_value, step)
    answer = str(progression[secret_numb])
    progression[secret_numb] = ".."
    value = " ".join(map(str, progression))
    return value, str(answer)


def build_progression(start_value, final_value, step):
    return list(range(start_value, final_value, step))
