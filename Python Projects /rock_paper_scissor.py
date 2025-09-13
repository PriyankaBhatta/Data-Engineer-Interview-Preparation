import random

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('r', 'p', 's')

while True:
    #ask user to make a choice
    user_choice = input('Rck, paper, or scissors? (r/p/s): ').lower()
    #if choice is not valid, print an error
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    #let the computer make a choice, print choices
    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    #determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice =='p') or
            (user_choice == 'p' and computer_choice == 'r')):
        print("Yay! You won.")
    else:
        print("Oh no! You lost.")

    # ask the user if they want to continue
    should_continue =  input("Continue? (y/n): ").lower()
    # if not terminate game
    if should_continue == 'n':
        break

