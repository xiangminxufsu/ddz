"""class of cards"""
import random

class Card(object):

	suits = ['hearts', 'diamonds', 'clubs', 'spades', 'black joker', 'red joker']
	
	def __init__(self, val, type):
		self.val = val
		self.type = type
		self.suit = self.suits[self.type]

class Cards(object):

	def __init__(self, deck=1, joker=True):
		self.cards = []
		self.fill()

	def fill(self):
		for i in range(deck):
			for j in range(52):
				card = Card(j%13+1, int(j/13))
				self.cards.append(card)
			if joker:
				self.cards.append(Card(14, 4))
				self.cards.append(Card(15, 5))

	def draw(self):
		return self.card.pop()

	def empty(self):
		if self.card:
			return False
		else:
			return True

	def shuffle(self):
		random.shuffle(self.cards)

	def print(self):
		for card in self.cards:
			print(card.val, card.suit)


cards = Cards()
cards.shuffle()
cards.print()
