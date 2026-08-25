import random

user_counter = 0
computer_counter = 0
i = 1

while i <= 3:
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "cessor"
    elif computer == 3:
        computer = "paper"
        
    user = input("chose between : rock ,cessor,paper: ")
    
    if user == "rock" and computer == "rock":
        print("no winner this round")
    elif user == "rock" and computer == "cessor":
        print("you won ")
        user_counter += 1
    elif user == "rock" and computer == "paper":
        print("you did lose")
        computer_counter += 1
    elif user == "paper" and computer == "rock":
        print("you did win")
        user_counter += 1
    elif user == "paper" and computer == "cessor":
        print("you did loose")
        computer_counter += 1
    elif user == "paper" and computer == "paper":
        print(" no winner this round")
    elif user == "cessor" and computer == "rock":
        print("you did lose")
        computer_counter += 1
    elif user == "cessor" and computer == "cessor":
        print("no winne this time")
    elif user == "cessor" and computer == "paper":
        print("you did win")
        user_counter += 1
        
    i += 1

if user_counter > computer_counter:
    print("you did win all of these 3 rounds")
else:
    print("you did lose all of these 3 rounds")