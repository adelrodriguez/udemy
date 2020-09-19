import unittest
from deck import Deck, Card


class CardTest(unittest.TestCase):
    def test_init(self):
        '''Card inits successfully'''
        card = Card('A', 'Hearts')
        self.assertEqual(repr(card), 'A of Hearts')

    def test_failed_init(self):
        '''Init fails is value or suit are invalid'''
        with self.assertRaises(ValueError):
            Card('11', 'Clubs')

        with self.assertRaises(ValueError):
            Card('4', 'Trees')


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        '''Creates the deck'''
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        '''Deck should have 52 cards'''
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_full_deck(self):
        '''Shuffles the deck full deck'''
        initial_cards = self.deck.cards[:]
        self.deck.shuffle()

        self.assertNotEqual(initial_cards, self.deck.cards)
        self.assertEqual(len(initial_cards), len(self.deck.cards))

    def test_shuffle_not_full_deck(self):
        '''Cannot shuffle a deck that's not full'''
        self.deck._deal(1)

        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_deal_card(self):
        '''Deals a card'''
        self.assertIsInstance(self.deck.deal_card(), Card)
    


if __name__ == '__main__':
    unittest.main()
