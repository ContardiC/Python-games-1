import random

random_number = random.randint(1,10)
find = False

attempts = 5
while not find :
      player_number = int(input("Inserisci un numero tra 1 e 10\n"))
      if player_number==random_number :
            print("You Win!")
            find = True
      else:
            print("Wrong Number!")

      attempts = attempts + 1
      