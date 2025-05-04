from brain_games.utils import get_random_number


def make_progression(first_number, coll_length, increment, question_position):
    result = []
    current_number = first_number

    for i in range(coll_length):
        if i == question_position:
            result.append("..")
        else:
            result.append(str(current_number))
        current_number += increment
    return " ".join(result)


def progression_game():
    start = get_random_number()
    length = get_random_number(5, 11)
    increment = get_random_number(1, 20)
    question_position = get_random_number(0, length - 1)
    question = make_progression(start, length, increment, question_position)
    correct_answer = str(question_position * increment + start)
    return [question, correct_answer]
