from django.test import TestCase
from .models import Card, Deck


class CardTestCase(TestCase):
    deck = None
    card1 = None
    card2 = None
    card3 = None

    def setUp(self):
        """
        Sets up our testing fixture and creates objects
        which we can use in future tests
        """
        self.deck = Deck.objects.create(title='test_deck_1')
        self.card1 = Card.objects.create(parentDeck=self.deck, front='c1f', back='c1b', usageExample='c1ue')
        self.card2 = Card.objects.create(parentDeck=self.deck, front='c2f', back='c2b', usageExample='c2ue')
        self.card3 = Card.objects.create(parentDeck=self.deck, front='c3f', back='c3b', usageExample='c3ue')

    def test_starting_conditions(self):
        """
        check if deck and cards exists
        """
        self.assertIsInstance(self.deck, Deck)
        self.assertIsInstance(self.card1, Card)
        self.assertIsInstance(self.card2, Card)
        self.assertIsInstance(self.card3, Card)

    def test_card_has_previous(self):
        """
        The first card in the deck does not have a prev card.
        All other cards do.
        """
        self.assertFalse(self.card1.has_prev_card())
        self.assertTrue(self.card2.has_prev_card())
        self.assertTrue(self.card3.has_prev_card())

    def test_get_prev_card(self):
        """
        The first card should return None.
        All others should return the prev card in the deck.
        """
        self.assertIsNone(self.card1.get_prev_card())
        self.assertEqual(self.card1, self.card2.get_prev_card())
        self.assertEqual(self.card2, self.card3.get_prev_card())

    def test_card_has_next(self):
        """
        The last card in the deck does not have next card.
        All other cards do.
        """
        self.assertTrue(self.card1.has_next_card())
        self.assertTrue(self.card2.has_next_card())
        self.assertFalse(self.card3.has_next_card())

    def test_get_next_card(self):
        """
        The last card should return None.
        All others should return the next card in the deck.
        """
        self.assertIsNone(self.card3.get_next_card())
        self.assertEqual(self.card3, self.card2.get_next_card())
        self.assertEqual(self.card2, self.card1.get_next_card())
