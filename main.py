from art import logo, vs
from game_data import data
from random import sample

print(logo)
score = 0
  
def game(score):
  # Generate a random account from the game data.
  # Use random sample to prevent same same pieces of dat to be compared
  compare = sample(data, 2)
  a = compare[0]
  b = compare[1]
    
  def a_or_b_func(a_or_b):
    """ Takes the compare data, formats it and returns it into printable format """
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
      score += 1
      print(f"\nYou're right! Current score: {score}.\n")
      return game(score)
    else:
      print(f"\nSorry, that's wrong. Final score: {score}\n")
      continue_game = False
  
game(score)