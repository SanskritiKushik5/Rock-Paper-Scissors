import random

print("Let's Play!\n")
you = 0
comp = 0
game = ['Rock', 'Paper', 'Scissors']
while(True):
    i = input("Enter 1.Rock    2.Paper    3.Scissors:   ")
    x = random.choice(game)
    print("Computer: ", x)
    if i == "1":
        if x == game[2]:
            print("You won!")
            you += 1
        elif x == game[1]:
            print("You lost!")
            comp += 1
        else:
            print("Draw")
    elif i == "2":
        if x == game[0]:
            print("You won!")
            you += 1
        elif x == game[2]:
            print("You lost!")
            comp += 1
        else:
            print("Draw")
    elif i == "3":
        if x == game[1]:
            print("You won!")
            you += 1
        elif x == game[0]:
            print("You lost!")
            comp += 1
        else:
            print("Draw")
    else:
        print("Wrong input.")
    print("Scores:")
    print("You -", you)
    print("Computer -", comp)
    x = input("Enter 1 to continue and 0 to exit game:")
    if x == "1":
        continue
    elif x == "0":
        break
    else:
        print("Wrong input")