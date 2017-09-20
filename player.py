"""class that defines players."""
import collections
import rule

class PlayerBase(object):

	_counter = 0

	def __init__(self, name = ''):
		self.hold_cards = []
		self.played_cards = []
		self.is_lord = False
		self.name = name
		if not name:
			self.name = self.get_default_name()
		self.win = False

	def add_card(self, card):
		self.hold_cards.append(card)

	def sort_card(self):
		self.hold_cards.sort(key=lambda card: card.val)

	def print_cards(self):
		for card in self.hold_cards:
			print (card.val, card.suit),

	def empty(self):
		if self.hold_cards:
			return False
		return True

	def draw(self, pre_val):
		card = self.hold_cards.pop(0)
		print(self.name, ':', str(card))

	def card_to_val(self):
		res = collections.defaultdict(int)
		for card in self.hold_cards:
			res[hold_cards.symbol] += 1

	@classmethod
	def get_default_name(cls):
		cls._counter += 1
		return '{0}_{1}'.format(cls.__name__, cls._counter)

class AiPlayer(PlayerBase):
	"""dump ai player."""
	pass

	def __str__(self):
		return 'AiPlayer'

class Player(PlayerBase):
	pass

	def __str__(self):
		return 'Human_Player'



