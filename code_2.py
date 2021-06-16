from random import randint
from os import system
from time import sleep


def guess(a, b, x):
    counter = 0
    print(f"Guess a number between {a} and {b}")
    while True:
        counter += 1
        user_input = int(input("Enter your number\n"))
        if user_input > x:
            print("oppps you choose greater number plese try again")
        elif user_input < x:
            print("oppps you choose lesser number plese try again")
        else:
            print(
                f"correct\n\U0001F551Screen will clear automatically in 2 seconds\U0001F551")
            break
    return counter


if __name__ == "__main__":
    a = int(input("Enter value of a\n"))
    b = int(input("Enter value of b\n"))
    x = randint(a, b)
    print("...FIRST PLAYER TURN...")
    g = guess(a, b, x)
    sleep(2)
    system("cls")
    print("...SECOND PLAYER TURN...")
    g_ = guess(a, b, x)

if g < g_:
    print(
        f"first player won the game\nNumber of tries of first player = {g}\nNumber of tries of second player = {g_}")
elif g > g_:
    print(
        f"second player won the game\nNumber of tries of second player = {g_}\nNumber of tries of first player = {g}")
else:
    print("opps its a tie")
print(f"Thanks for playing see you soon \U0001F600\U0001F600")
