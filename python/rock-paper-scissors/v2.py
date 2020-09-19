from random import randint

print('Rock...')
print('Paper...')
print('Scissors...')

player = input('Player, make your move: ').lower()
rand_num = randint(0, 2)

if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
elif rand_num == 2:
    computer = 'scissors'

print(f'Computer plays: {computer}')

if player == computer:
    print('It\'s a tie!')
elif player == 'rock':
    if computer == 'paper':
        print('Computer wins!')
    elif computer == 'scissors':
        print('Player wins!')
elif player == 'paper':
    if computer == 'rock':
        print('Player wins!')
    elif computer == 'scissors':
        print('Computer wins!')
elif player == 'scissors':
    if computer == 'rock':
        print('Computer wins!')
    elif computer == 'paper':
        print('Player wins!')
else:
    print('Something went wrong')
