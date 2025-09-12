#generate a random number
import random

number_to_guess = random.randint(1,100)
#loop through the numbers
while True:
    #ask user for input
    try:
        guess_number = int(input("Enter a number between 1 and 100.: "))
        # if number < guess, print too low
        if guess_number < number_to_guess:
            print("Too low!")
        # if number > guess, print too high
        elif guess_number > number_to_guess:
           print('Too high!')
        # else, print well done
        else:
           print("Congrats , you guessed the correct number.")
           break

    except ValueError: # if not valid number, print error
       print("Please enter a valid number.")
