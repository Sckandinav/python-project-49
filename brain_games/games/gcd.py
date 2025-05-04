import math
from brain_games.utils import get_random_number

def gcd_game():
  x = get_random_number()
  y = get_random_number()
  question = f'{x} {y}'
  correct_answer = math.gcd(x, y)
  return [question, str(correct_answer)]
  