from Card import *

class Hand:

	def __init__(self):
		self.cards = []

	def Get(self, card):
		"""
		Get() puts a card into this hand

		:param card: the card received (Card)
		:return: None
		"""
		self.cards.append(card)

	def Draw(self, deck):
		"""
		Draw() draws a card from the deck and put it into this hand

		:param deck: the deck that draws from (Deck)
		:return: None
		"""
		self.Get(deck.Top())

	def __str__(self):
		retval = ""

		for card in self.cards:
			retval += str(card) + "\n"

		return retval