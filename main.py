from art import logo, vs
from game_data import data
from random import sample
import os

os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
score = 0
  
def game(score):
  """ Generate a random account and return it from the game data """
  # Use random sample to prevent same pieces of data to be compared
  compare = sample(data, 2)
  a = compare[0]
  b = compare[1]
    
  def a_or_b_func(a_or_b):
    """ Takes the compare data, reformat it and return a printable form """
    return f"{a_or_b['name']}, {a_or_b['description']}, from {a_or_b['country']}."
  # print(test(a), test(b))
  
  print(f"Compare A: {a_or_b_func(a)}")
  print(vs)
  print(f"Against B: {a_or_b_func(b)}")
  # print(a['follower_count'], b['follower_count']) # follower count

  
  continue_game = True

  while continue_game:
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == 'a' and a['follower_count'] > b['follower_count'] or user_input == 'b' and b['follower_count'] > a['follower_count']:
      os.system('cls' if os.name == 'nt' else 'clear')
      score += 1
      print(f"\nYou're right! Current score: {score}.\n")
      return game(score)
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print(logo)
      print(f"\nSorry, that's wrong. Final score: {score}\n")
      # See if they want to continue
      try_again = input('Do you want to continue: Y/N: ').lower()
      if try_again == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        return game(score=0) # reset score to 0
      continue_game = False
  
game(score)