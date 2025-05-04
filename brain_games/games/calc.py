import random
from brain_games.utils import get_random_number


OPERATIONS = ['+', '-', '*']


def calculation (x, y, operation):
  match operation:
    case '+':
      return x + y
    case '-':
      return x - y
    case '*':
      return x * y
    case _: 
      return None


def calc_game():
  rng = random.SystemRandom()
  x = get_random_number()
  y = get_random_number()
  operator = OPERATIONS[rng.randint(0,2)]
  question = f"{x} {operator} {y}"
  correct_answer = calculation(x, y, operator)
  return [question, str(correct_answer)]