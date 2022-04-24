from Card import *
import random


class Deck:

	def __init__(self, decknum=1, exclude=None, ranking=None, suiting=None):
		"""
		Deck() initializes a deck with specified number of decks, excluded cards, and desired ranking

		:param decknum: number of decks used in the game (int)
		:param exclude: cards that are not used in the deck (list(Card))
		:param ranking: a list of ranking, the higher the index, the higher the rank (list(char))
		:param suiting: a list of suit ranking, the higher the index, the higher the suit (list(string))
		"""
		if exclude is None:
			exclude = []
		self.deck = self.__NewDeck(exclude)
		while decknum > 1:
			self.deck += self.deck
			decknum -= 1
		if ranking is None:
			self.ranking = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		else:
			self.ranking = ranking
		if suiting is None:
			self.suiting = None
		else:
			self.suiting = suiting
		self.Shuffle()

	def __NewDeck(self, exclude):
		"""
		__NewDeck() returns a deck with cards excluded

		:param exclude: list of excluded card from one deck (list(Card))
		:return: a list of cards as a deck with specified card excluded
		"""
		deck = []
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		suits = ["Club", "Diamond", "Heart", "Spade"]

		for suit in suits:
			for rank in ranks:
				deck.append(Card(rank, suit))

		for excludedCard in exclude:
			deck.remove(excludedCard)

		return deck

	def Shuffle(self):
		"""
		Shuffle() shuffles the deck in random order

		:return: None
		"""
		random.shuffle(self.deck)

	def Deal(self, players, amount=-1):
		"""

		:param players: the list of players, len(players) >= 1 (list(Hand))
		:param amount: the number of cards dealt to each player, -1 for dealing the entire deck (int)
		:return: None
		"""
		if len(players) < 1:
			return

		if amount == -1:
			while len(self.deck) > 0:
				for player in players:
					player.get(self.deck.pop())
					if len(self.deck) <= 0:
						return
			return

		if amount * len(players) > len(self.deck):
			print("Cannot deal " + amount + " card(s) for " + len(players) + " from the deck.")
		count = 0
		while len(self.deck) > 0 and count < amount:
			for player in players:
				player.Get(self.deck.pop())

	def Top(self):
		"""
		Top() removes and returns the top card from the deck

		:return: the card at the last position from self.deck
		"""
		return self.deck.pop()

	def __str__(self):
		retval = ""

		for card in self.deck:
			retval += str(card) + "\n"

		return retval

