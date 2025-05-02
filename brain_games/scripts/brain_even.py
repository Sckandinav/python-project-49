import random

from ..game_basis import game_basis


MIN_NUMBER = 1
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_round():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return [question, correct_answer]


def main():
    game_basis(DESCRIPTION, make_round)


if __name__ == '__main__':
    main()