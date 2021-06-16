import random
while True:
    try:
        a = int(input("Enter the value of a\n"))
        break

    except ValueError:
        print("sorry wrong input please try again...")
    except Exception as error:
        print(error)

while True:
    try:
        b = int(input("Enter the value of b\n"))
        break
    except ValueError:
        print("sorry wrong input please try again...")
    except Exception as error:
        print(error)

x = random.randint(a, b)
user1_points = 0
while True:
    user1_points += 1
    player1 = int(input("Enter your number\n"))
    if player1 == x:
        print("correct")
        break
    elif player1 > x:
        print("oppps you choose greater number plese try again")
    elif player1 < x:
        print("oppps you choose lesser number plese try again")

import os
os.system("cls")

print("...........................now its second player turn.......................")

user2_points = 0
while True:
    user2_points += 1
    player1 = int(input("Enter your number\n"))
    if player1 == x:
        print("correct")
        break
    elif player1 > x:
        print(f"oppps you choose greater number plese try again")
    elif player1 < x:
        print("oppps you choocse lesser number plese try again")
if user1_points < user2_points:
    print("first player won the game")
elif user1_points > user2_points:
    print("second player won the game")
else:
    print("opps its a tie")
print("Thanks for playing see you soon..................")
