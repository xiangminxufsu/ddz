"""class of cards"""
import random

class CardBase(object):

	suits = ['hearts', 'diamonds', 'clubs', 'spades', 'black joker', 'red joker']
	
	def __init__(self, val, type):
		self.val = val
		self.type = type
		self.suit = self.suits[self.type]
		self.symbol = None
	def __str__(self):
		return '{0},{1}'.format(self.suit, self.val)

class DDZCard(CardBase):
	symbol_d = {10:'0', 11:'J', 12:'Q', 13:'K', 14:'A', 15:'2', 16:'w', 17:'W'}
	def __init__(self, val, type):
		super(DDZCard, self).__init__(val, type)
		if val == 1:
			self.val = 14
		elif val == 2:
			self.val = 15
		if self.val in self.symbol_d:
			self.symbol = self.symbol_d[self.val]
		else:
			self.symbol = str(self.val)
	def __str__(self):
		return '{0},{1}'.format(self.suit, self.symbol)

class Cards(object):

	def __init__(self, deck=1, joker=True):
		self.deck = deck
		self.joker = joker
		self.cards = []
		self.fill()

	def fill(self):
		for i in range(self.deck):
			for j in range(52):
				card = DDZCard(j%13+1, int(j/13))
				self.cards.append(card)
			if self.joker:
				self.cards.append(DDZCard(16, 4))
				self.cards.append(DDZCard(17, 5))

	def draw(self):
		return self.cards.pop()

	def empty(self):
		if self.card:
			return False
		else:
			return True

	def shuffle(self):
		random.shuffle(self.cards)

	def print_(self):
		for card in self.cards:
			print(card.val, card.suit)


#cards = Cards()
#cards.shuffle()
#cards.print()
