from brain_games.utils import get_random_number


def even_game():
    question = get_random_number()
    correct_answer = "yes" if question % 2 == 0 else "no"
    return [question, correct_answer]
