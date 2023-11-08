# roll_dice.py

import random

def roll_dice(min_val, max_val):
  while True:
    print("Dice Rolling...")
    print(f"Your number is {random.randint(min_val, max_val)}")
    result = input("Do you want to roll the dices again? (y/n) ")
    if result.lower() == "n":
      break

roll_dice(1, 6)
