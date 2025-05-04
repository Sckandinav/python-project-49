from brain_games.game_basis import game_basis
from brain_games.games.prime import prime_game


DESCRIPTION = '"yes" if given number is prime. Otherwise answer "no".'

def main():
  game_basis(DESCRIPTION, prime_game)


if __name__ == '__main__':
  main()