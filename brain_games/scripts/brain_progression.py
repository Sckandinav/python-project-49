from brain_games.game_basis import game_basis
from brain_games.games.progression import progression_game

DESCRIPTION = "What number is missing in the progression?"


def main():
    game_basis(DESCRIPTION, progression_game)


if __name__ == "__main__":
    main()
