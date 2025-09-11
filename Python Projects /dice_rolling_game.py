import random

#loop
while True:
    # ask: roll the dice?
    choice = input("Roll the dice? (y/n): ").lower()
    # if user enters y, generate two random numbers
    if choice == 'y':
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        # print them
        print(f'({number1}, {number2})')
    # if user enters n
    elif choice == 'n':
        # print thankyou msg
        print("Thanks for playing! ")
        # terminate
        break
    # else, print invalid choice
    else:
        print("Invalid choice!")
