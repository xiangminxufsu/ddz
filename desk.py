""" desk class for playing cards.
Table should be an event manager that manages player playing cards."""

class Table(object):

	def __init__(self, max_player=3):
		self.players = []
		self._ready = False
		self._max_player = max_player

	def add_player(self, player):
		self.players.append(player)

	def add_cards(self, cards):
		self._cards = cards

	def distribute_card(self):
		self._cards.shuffle()
		# for ddz only
		self._bonus_card = [self._cards.draw() for _ in range(3)] #bonus card for landloard
		for player in self.players:
			for _ in range(17):
				player.add_card(self._cards.draw())
			if player.is_lord:
				for card in self._bonus_card:
					player.add_card(card)
			player.sort_card()












