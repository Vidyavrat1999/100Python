from random import choice

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
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for Scissors.\n"))
if user_choose == 0:
    print(rock)
elif user_choose == 1:
    print(paper)
else:
    print(scissors)

print('Computer chose:')
computer_choose = choice([0,1,2])
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
else:
    print(scissors)

#result decision
if user_choose == computer_choose:
    print("Same chosen. Draw! 🤷‍♂️")
elif user_choose == 0 and computer_choose == 1:
    print("Paper beats Rock. You lose! 🙁")
elif user_choose == 0 and computer_choose == 2:
    print("Rock beats Scissors. You won! 😃")
elif user_choose == 1 and computer_choose == 0:
    print("Paper beats Rock. You win! 😃")
elif user_choose == 1 and computer_choose == 2:
    print("Scissors beats Paper. You lose! 🙁")
elif user_choose == 2 and computer_choose == 0:
    print("Rock beats Scissors. You lose! 🙁")
elif user_choose == 2 and computer_choose == 1:
    print("Scissors beats Paper. You won! 😃")
else:
    print("Wrong input. Play again. Enter values 0 or 1 or 2 only")
