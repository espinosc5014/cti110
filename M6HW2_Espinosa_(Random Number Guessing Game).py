# CTI-110
# M6HW2_Espinosa_(Random Number Guessing Game)
# Christopher Espinosa
# 11-6-2017
#

import random

def main():
        print("Let us play a guessing game...")
        print("I am thinking of a number between 1 and 100. You have 10 tries.  Good Luck!")
        play_game()

        answer = input("\nWould you like to play again? Y or N ? ")
        if answer == "y" or answer == "Y":
                main()
        else:
                print("Thanks for playing!")

def play_game():
        number = random.randrange(1,101)
        guess = 0
        counter = 0
        while guess != number and counter != 10:
                guess = int(input("\nPlease enter your guess: "))
                counter += 1
                if counter != 10:
                        if guess > number:
                                print("Sorry too high.")
                        elif guess < number:
                                print("Sorry too low.")
                        elif guess == number:
                                print("\nCongratulations you guess it!")
                                print("It took you",counter,"tries.")
                else:
                        print("\nThat was your 10th guess, You LOSE!")
                        print("The number was",number,".")
        
                
main()

input("\nPress Enter to Exit")


