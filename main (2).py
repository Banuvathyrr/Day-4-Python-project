## Rock paper scissors game 
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

#Write your code below this line 👇
import random
temp =[rock, paper, scissors]
print ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
print(temp[user_choice]) 

comp_choice = random.randint(0,2)
print("Computer chose:")
print(temp[comp_choice])

if (user_choice == 0 and comp_choice == 2):
  print("You win")
elif (user_choice == 2 and comp_choice == 0):
  print("You lose")
elif (user_choice == 1 and comp_choice == 2):
  print("You lose")
elif (user_choice == 2 and comp_choice == 1):
  print("You win")
elif (user_choice == 0 and comp_choice == 1):
  print("You lose")
elif (user_choice == 1 and comp_choice == 0):
  print ("You win")
elif (user_choice == comp_choice):
  print("It's a draw")
