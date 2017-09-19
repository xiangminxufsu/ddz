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
		self.cards = cards

	def add_event(self, event):
		self.event = event


	def start(self):
		self.event.add_players(self.players)
		self.event.add_cards(self.cards)
		self.event.start()



