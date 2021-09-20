import random
roll_dice = input("write start to dice roll: ")

roll_again = ""

while roll_again == "":
  
    if roll_dice == "start":
      posiblle_results = [1, 2, 3, 4, 5, 6]
      result = random.choice(posiblle_results)
      print("you rolled a..." + str(result))
    
    
     
    if roll_dice == "starr":
      posiblle_results = [4, 5, 6]
      result = random.choice(posiblle_results)
      print("you rolled a..." + str(result))
    
    
    
    roll_again = input("write x to exit")
