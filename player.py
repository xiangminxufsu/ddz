"""class that defines players."""

class Player(object):

	def __init__(self):
		self.hold_cards = []
		self.played_cards = []
		self.is_lord = False

	def add_card(self, card):
		self.hold_cards.append(card)

	def sort_card(self):
		self.hold_cards.sort(key=lambda card: card.val)

	def print_cards(self):
		for card in self.hold_cards:
			print(card.val, card.suit),



