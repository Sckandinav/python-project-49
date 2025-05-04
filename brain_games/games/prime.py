from brain_games.utils import get_random_number


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_game():
    question = get_random_number(1, 1000)
    correct_answer = "yes" if is_prime(question) else "no"
    return [question, correct_answer]
