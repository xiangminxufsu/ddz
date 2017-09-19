"""handles event."""
from player import AiPlayer, Player
import time


class Event(object):

	def __init__(self):
		pass

	def start(self):
		pass
	def add_cards(self, cards):
		self.cards = cards

	def add_players(self, players):
		self.players = players


class DDZEvent(Event):
	"""docstring for DDZEvent"""
	def __init__(self):
		super(DDZEvent, self).__init__()
	
	def start(self):
		self.distribute_card()
		self.decide_lord()
		for p in self.players:
			p.print_cards()
		p = 0
		if self.players[1].is_lord:
			p = 1
		elif self.players[2].is_lord:
			p  = 2
		
		pre_val = -1
		game_on = True
		while game_on:
			for _ in range(3):
				p = (p+1)%3
				self.players[p].draw(pre_val)
				#time.sleep(0.2)
				if self.players[p].empty():
					self.players[p].win = True
					game_on = False
			#break
		print('=====Game Over======')


	def decide_lord(self):
		for player in self.players:
			if isinstance(player, Player):
				player.is_lord = True
				for card in self._bonus_card:
					player.add_card(card)


	def distribute_card(self):
		self.cards.shuffle()
		#todo write a subclass for ddz only
		# for ddz only
		self._bonus_card = [self.cards.draw() for _ in range(3)] #bonus card for landloard
		for player in self.players:
			for _ in range(17):
				player.add_card(self.cards.draw())
			if player.is_lord:
				for card in self._bonus_card:
					player.add_card(card)
			player.sort_card()