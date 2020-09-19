from random import shuffle


class Card:
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, value, suit):
        if suit not in Card.suits:
            raise ValueError(f'{suit} is not a valid card suit')

        if value not in Card.values:
            raise ValueError(f'{value} is not a valid card value')

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        values = ('A', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K')
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, num):
        card_count = self.count()
        if not card_count:
            raise ValueError('All cards have been dealt')

        return [self.cards.pop() for _ in range(min(num, card_count))]

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')

        shuffle(self.cards)

        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
