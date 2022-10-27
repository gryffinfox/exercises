# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import random

rules = [
    "Scissors cuts paper.",
    "Paper covers rock.",
    "Rock crushes lizard.",
    "Lizard poisons Spock.",
    "Spock smashes scissors.",
    "Scissors decapitates lizard.",
    "Lizard eats paper.",
    "Paper disproves Spock.",
    "Spock vaporizes rock.",
    "Rock crushes scissors.",
]

moves = ["rock", "paper", "scissors", "lizard", "spock"]
print(
    "Welcome to the rock-paper-scissors-lizard-Spock game.",
    "\nIf you want to leave the game, type exit.",
    "\nIf you want to know the rules, type rules.",
)

while True:
    player = input("3, 2, 1... GO! What do you choose? ")

    if player.lower() == "exit":
        break
    elif player.lower() == "rules":
        print(rules)
        continue

    computer = random.choice(moves)
    print("Computer: {} | Player: {}".format(computer, player))

    if computer == player:
        print("It's a tie.\n")

    elif computer == "rock":
        # computer chooses rock, computer wins
        if player in [moves[2], moves[3]]:
            print("Rock crushes {}. You lost!".format(player))

        # computer chooses rock, computer loses
        elif player in [moves[1], moves[4]]:
            print("You won.")

    elif computer == "paper":
        # computer chooses paper, computer wins
        if player in [moves[0], moves[4]]:
            print("Paper wins over {}. You lost!".format(player))
        # computer chooses paper, computer loses
        elif player in [moves[2], moves[3]]:
            print("You won.")

    elif computer == "scissors":
        # computer chooses scissors, computer wins
        if player in [moves[1], moves[3]]:
            print("Scissors cut {}. You lost!".format(player))
        # computer chooses scissors, computer loses
        elif player in [moves[0], moves[4]]:
            print("You won.")

    elif computer == "lizard":
        # computer chooses lizard, computer wins
        if player in [moves[1], moves[4]]:
            print("Lizard eats {}. You lost!".format(player))
        # computer chooses lizard, computer loses
        elif player in [moves[0], moves[2]]:
            print("You won.")

    elif computer == "spock":
        # computer chooses Spock, computer wins
        if player in [moves[0], moves[2]]:
            print("Spock vaporises {}. You lost!".format(player))
        # computer chooses Spock, computer loses
        elif player in [moves[1], moves[3]]:
            print("You won.")
