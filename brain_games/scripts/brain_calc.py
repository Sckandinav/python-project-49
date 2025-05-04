from brain_games.game_basis import game_basis
from brain_games.games.calc import calc_game

DESCRIPTION = "What is the result of the expression?"


def main():
    game_basis(DESCRIPTION, calc_game)


if __name__ == "__main__":
    main()
