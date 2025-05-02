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
  x = random.randint(MIN_NUMBER, MAX_NUMBER)
  y = random.randint(MIN_NUMBER, MAX_NUMBER)
  operator = OPERATIONS[random.randint(0,2)]
  question = f"{x} {operator} {y}"
  correct_answer = calculation(x, y, operator)
  return [question, str(correct_answer)]