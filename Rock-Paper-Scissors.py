import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to Rock-Paper Scissors!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice == 0:
  print("You chose Rock" + rock)
elif user_choice == 1:
  print("You chose Paper" + paper)
elif user_choice == 2:
  print("You chose Scissors" + scissors)
else:
  print("You entered a wrong choice.")

#Computers turn
computer_turn = random.randint(0,2)
if computer_turn == 0:
  print("Computer chose Rock" + rock)
elif computer_turn == 1:
  print("Computer chose Paper" + paper)
elif computer_turn == 2:
  print("Computer chose Scissors" + scissors)
else:
  print("You entered a wrong choice.")

#Winner decided
if user_choice == 1 and computer_turn == 0:
  print("You won")
elif user_choice == 2 and computer_turn == 1:
  print("You won")
elif user_choice == 0 and computer_turn == 2:
  print("You won")
elif user_choice == 1 and computer_turn == 1:
  print("You drew")
elif user_choice == 2 and computer_turn == 2:
  print("You drew")
elif user_choice == 0 and computer_turn == 0:
  print("You drew")
else:
  print("You lost")

