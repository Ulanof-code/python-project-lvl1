from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def set_value_and_result():
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
    secret_numb = randint(0, len(build_list(start_value, final_value, step)) - 1) # noqa E501
    result = build_list(start_value, final_value, step)[secret_numb] # noqa E501
    value = build_progression(build_list(start_value, final_value, step), secret_numb) # noqa E501
    return value, str(result) # noqa E501


def build_progression(list_progression, secret_numb):
    line_numb = ""
    for i in range(len(list_progression)):
        if i == secret_numb:
            list_progression[i] = ".."
        line_numb = line_numb + str(list_progression[i]) + " "
    return line_numb


def build_list(start_value, final_value, step):
    return list(range(start_value, final_value, step))
