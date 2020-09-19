from termcolor import colored, COLORS
from pyfiglet import figlet_format


def get_color():
    c = input('In what color? ')

    if c not in COLORS:
        return 'blue'

    return c


message = input('What would you like to print? ')
color = get_color()

ascii_message = figlet_format(message)
ascii_art = colored(ascii_message, color=color)

print(ascii_art)
