import random
roll_dice = input("write start to dice roll: ")

while True:
  
    if roll_dice == "start":
      posiblle_results = [1, 2, 3, 4, 5, 6]
      result = random.choice(posiblle_results)
      print("you rolled a..." + str(result))
      break
      
    if roll_dice == "starr":
      posiblle_results = [4, 5, 6]
      result = random.choice(posiblle_results)
      print("you rolled a..." + str(result))
      break
