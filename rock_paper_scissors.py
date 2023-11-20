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
choice=int(input("What do you choose? Type 0 for Rock, 1  for Paper and 2 for Scissors:\n"))
comp_choice=random.randint(0,2)
if(choice==0):
  print(f"You chose Rock\n {rock}\n")
  if(comp_choice==0):
    print(f"Computer chose Rock\n {rock}\n")
    print("Its a draw")
  elif(comp_choice==1):
    print(f"Computer chose Paper\n {paper}\n")
    print("You lose")
  elif(comp_choice==2):
    print(f"Computer chose Scissors\n {scissors}\n")
    print("You win")
elif(choice==1):
  print(f"You chose Paper\n {paper}")
  if(comp_choice==0):
    print(f"Computer chose Rock\n {rock}\n")
    print("You win")
  elif(comp_choice==1):
    print(f"Computer chose Paper\n {paper}\n")
    print("Its a draw")
  elif(comp_choice==2):
    print(f"Computer chose Scissors\n {scissors}\n")
    print("You lose")
elif(choice==2):
  print(f"You chose Scissors\n {scissors}")
  if(comp_choice==0):
    print(f"Computer chose Rock\n {rock}\n")
    print("You lose")
  elif(comp_choice==1):
     print(f"Computer chose Paper\n {paper}\n")
     print("You win")
  elif(comp_choice==2):
    print(f"Computer chose Scissors\n {scissors}\n")
    print("Its a draw")
else:
  print("Don't try to be smart. Choose a number between 0 and 2")
    
    
