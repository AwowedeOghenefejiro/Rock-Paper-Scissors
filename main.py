import random
print('''Welcome to the game!
    R is for Rock
    P is for Paper
    S is for Scissors''')

while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = str(input("{},{},{}?\n"))

    while player not in choices:
        print("Error! Not an option")
        break

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")

        restart = input("It's a Tie. Start Again. Y/N")
        if restart == "N":
            break
        elif restart == "Y":
            continue

    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("Loser!")
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("Winner!")
            break
    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("Loser!")
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("Winner!")
            break

    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("Loser!")
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("Winner!")
            break


print("Bye!")
