from brain_games.game_basis import game_basis
from brain_games.games.even import even_game

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game_basis(DESCRIPTION, even_game)


if __name__ == "__main__":
    main()
