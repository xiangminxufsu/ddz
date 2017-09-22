"""class that defines players."""
import collections

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
		hold_cards = ''.join([card.symbol for card in self.hold_cards])
		played_cards = ''.join([card.symbol for card in self.played_cards])
		print(str(self), '    ',hold_cards, '     ',played_cards)

	def empty(self):
		if self.hold_cards:
			return False
		return True

	@classmethod
	def add_rule(cls, rule):
		cls.rule = rule

	def draw(self, pre_type, pre_seq):
		card_type, seq, played_cards = self.rule.draw(pre_type, pre_seq ,self.hold_cards)
		self.played_cards += played_cards
		return card_type, seq

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
		return 'AiPlayer {0}'.format(self.name)

class Player(PlayerBase):
	pass

	def __str__(self):
		return 'Human_Player {0}'.format(self.name)



