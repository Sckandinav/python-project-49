import random

MIN_NUMBER = 1
MAX_NUMBER = 100
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
  x = rng.randint(MIN_NUMBER, MAX_NUMBER)
  y = rng.randint(MIN_NUMBER, MAX_NUMBER)
  operator = OPERATIONS[rng.randint(0,2)]
  question = f"{x} {operator} {y}"
  correct_answer = calculation(x, y, operator)
  return [question, str(correct_answer)]