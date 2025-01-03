import random
MIN = 1
MAX = 10

random_number = random.randint(MIN,MAX)
find = False

attempts = 0
difficulty_level = int(input("Choose the difficulty level: 1- Easy 2-Medium 3-Hard\n"))
if difficulty_level == 1:
      max_attempts = 8
elif difficulty_level == 2:
      max_attempts = 5
elif difficulty_level == 3:
      max_attempts = 2
else:
      print("Invalid choice")

while not find and attempts < 5:
      player_number = int(input("Enter an integer between 1 and 10\n"))
      if player_number==random_number :
            print("You Win!\n")
            find = True
      else:
            print("You haven't guessed right!")
      attempts = attempts + 1
      if attempts == max_attempts and find == False:
            print("You lost :(\n")