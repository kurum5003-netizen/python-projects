import random
from random import choice

rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper=  """
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_imgas=[rock,paper,scissors]
choice=int(input("rock =0,paper =1,scissors =2"))
if choice>=0 and choice<=2:
    print(game_imgas[choice])
else:
    print("geçersiz sayı girdin")
    exit()
computerchoice=random.randint(0,2)
print(game_imgas[computerchoice])

if choice==0 and computerchoice==2:
    print("user win!")
elif choice==2 and computerchoice==0:
    print("computer win!")
elif computerchoice > choice:
    print("computer win!")
elif choice > computerchoice:
    print("user win!")
elif computerchoice==choice:
    print("draw")


