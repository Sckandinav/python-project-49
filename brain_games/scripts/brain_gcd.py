from brain_games.game_basis import game_basis
from brain_games.games.gcd import gcd_game

DESCRIPTION = "Find the greatest common divisor of given numbers."


def main():
    game_basis(DESCRIPTION, gcd_game)


if __name__ == "__main__":
    main()
