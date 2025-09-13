import random

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = tuple(emojis.keys())

# ask user to make a choice
def get_user_choice():
    while True:
        user_choice = input('Rck, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

#displaying choices
def display_choices(user_choice,computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

#determining winner condition
def determine_winner(user_choice,computer_choice):
    # determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
        print("Yay! You won.")
    else:
        print("Oh no! You lost.")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices) #let the computer make a choice, print choices

        display_choices(user_choice,computer_choice)

        determine_winner(user_choice,computer_choice)

        # ask the user if they want to continue
        should_continue =  input("Continue? (y/n): ").lower()
        # if not terminate game
        if should_continue == 'n':
            break

play_game()

