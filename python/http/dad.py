import requests
from random import choice
from termcolor import colored
from pyfiglet import figlet_format


def print_art():
    ascii_text = figlet_format('Dad Joke 3000')
    ascii_art = colored(ascii_text, color='blue')

    print(ascii_art)


def print_joke(results, search_term):
    quantity = len(results)

    if not quantity:
        print(
            f'Sorry, I don\'t have any jokes about {search_term}! Please try again.')
    elif quantity == 1:
        print(f'I\'ve got one joke about {search_term}. Here it is:')
        print(results[0]['joke'])
    else:
        print(f'I\'ve got {quantity} jokes about {search_term}. Here\'s one:')
        print(choice(results)['joke'])


def get_joke(search_term):
    url = 'https://icanhazdadjoke.com/search'
    response = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={'term': search_term}
    )

    data = response.json()
    print_joke(data['results'], search_term)


def start():
    print_art()
    search_term = input('Let me tell you a joke! Give me a topic: ')
    get_joke(search_term)


start()
