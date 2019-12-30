from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Deck(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=64, null=False, blank=False, help_text="64 characters maximum")
    description = models.CharField(max_length=64, null=False, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def num_of_cards(self):
        return self.card_set.count()

    num_of_cards.short_description = 'Card Count'


class Card(models.Model):
    parentDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.CharField(max_length=32, help_text="32 characters maximum")
    back = models.CharField(max_length=32, blank=True)
    usageExample = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.front + " " + self.back

    def has_prev_card(self):
        """
        returns true if the card is not the first card in the deck.
        """
        first_card_in_deck = self.parentDeck.card_set.first()
        if self == first_card_in_deck:
            return False
        return True

    def get_prev_card(self):
        """
        Returns previous card in deck
        """
        return self.parentDeck.card_set.filter(id__lt=self.id).last()

    def has_next_card(self):
        """
        returns true if the card is not the first card in the deck.
        """
        last_card_in_deck = self.parentDeck.card_set.last()
        if self == last_card_in_deck:
            return False
        return True

    def get_next_card(self):
        """
        Returns next card in deck
        """
        return self.parentDeck.card_set.filter(id__gt=self.id).first()
