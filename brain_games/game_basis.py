import prompt
from .cli import welcome_user

def game_basis(description, make_round):
  quantity = 3
  user_name = welcome_user()
  print('Welcome to the Brain Games!')
  print(f'{description}')

  for _ in range(quantity):
    [question, correct_answer] = make_round()
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if(answer == correct_answer):
      print('Correct')
    else:
      return print(f'{answer} is wrong answer ;(. Correct answer was \'{correct_answer}\'.\nLet\'s try again, {user_name}')
  return print(f'Congratulations, {user_name}')