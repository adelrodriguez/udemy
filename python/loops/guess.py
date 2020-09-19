from random import randint

random_number = randint(1, 10)  # numbers 1 - 10

while True:
    guess = int(input('Guess a number between 1 and 10: '))

    if (guess < random_number):
        print('Too low, try again!')
    elif (guess > random_number):
        print('Too hight, try again!')
    else:
        print('You guessed it! You won!')

        play_again = input('Do you want to keep playing? (y/n) ')

        if (play_again != 'y'):
            print('Thank you for playing!')
            break

        random_number = randint(1, 10)  # numbers 1 - 10
