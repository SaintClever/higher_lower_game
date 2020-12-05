from art import logo, vs
from game_data import data
from random import sample

print(logo)
score = 0
  
def game(score):
  compare = sample(data, 2)
  a = compare[0]
  b = compare[1]
    
  print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
  print(vs)
  print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
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