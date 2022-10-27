# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# generate random number between 1-9 and ask user to take a guessing
# tell them is they guessed too low, high or even

import random

while True:
    generated_number = random.randint(1, 10)
    while True:
        try:
            players_guess = int(
                input("I am thinking of a number between 1 and 9. Can you guess it? ")
            )
            break
        except ValueError:
            print("Not a number, try again.")

    if generated_number == players_guess:
        print("Yes, I was thinking of", generated_number, ". You got it! :)")
    elif generated_number > players_guess:
        print(
            "No, you guessed a number that was smaller than the one I had on my mind."
        )
    elif generated_number < players_guess:
        print("No, your number is bigger than the one I had on my mind.")

    again = input("Do you want to play again? If not, type exit. ")
    if again.lower() == "exit":
        break
    else:
        pass
