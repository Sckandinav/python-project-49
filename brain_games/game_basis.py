import prompt

from brain_games.cli import welcome_user


def game_basis(description, make_round):
    quantity = 3
    user_name = welcome_user()
    print("Welcome to the Brain Games!")
    print(f"{description}")

    for _ in range(quantity):
        [question, correct_answer] = make_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct")
        else:
            error_msg = (
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {user_name}!"
            )
            return print(error_msg)
    return print(f"Congratulations, {user_name}!")
