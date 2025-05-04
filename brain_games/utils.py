import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def get_random_number():
  rng = random.SystemRandom()
  return rng.randint(MIN_NUMBER, MAX_NUMBER)