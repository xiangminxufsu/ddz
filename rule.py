import json
import collections
import random
from card import DDZCard as c

class RuleBase(object):
	def __init__(self):
		pass

class DDZRule(RuleBase):

	CARD_TYPES = [
	    'rocket', 'bomb',
	    'single', 'pair', 'trio', 'trio_pair', 'trio_single',
	    'seq_single5', 'seq_single6', 'seq_single7', 'seq_single8', 'seq_single9', 'seq_single10', 'seq_single11',
	    'seq_single12',
	    'seq_pair3', 'seq_pair4', 'seq_pair5', 'seq_pair6', 'seq_pair7', 'seq_pair8', 'seq_pair9', 'seq_pair10',
	    'seq_trio2', 'seq_trio3', 'seq_trio4', 'seq_trio5', 'seq_trio6',
	    'seq_trio_pair2', 'seq_trio_pair3', 'seq_trio_pair4', 'seq_trio_pair5',
	    'seq_trio_single2', 'seq_trio_single3', 'seq_trio_single4', 'seq_trio_single5',
	    'bomb_pair', 'bomb_single'
	]
	value_map = {'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':15, 'w':16, 'W':17}
	str_map = {3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K', 14:'A', 15:'2', 16:'w', 17:'W'}

	def create_combos(self, cards):
		"""creats seqs based on a list of card object."""
		"""returns a dict, key being type and vals a list of seq."""
		with open('rule.json', 'r') as f:
			rules = json.load(f)
		d = collections.defaultdict(int)
		ans = collections.defaultdict(list)
		for card in cards:
			d[card.symbol] += 1
		for card_type, seqs in rules.items():
			for seq in seqs:
				counter = collections.Counter(seq)
				include = True
				for symbol, count in counter.items():
					if symbol not in d or d[symbol] < counter[symbol]:
						include = False
						break
				if include:
					ans[card_type].append(seq)
		return ans

	def create_combo_list(self, cards):
		"""[('single', '1'), ('pair', 'AA'), ('pair', '22')]"""
		rt_list = []
		combo_dict = self.create_combos(cards)
		for card_type, seqs in combo_dict.items():
			for seq in seqs:
				rt_list.append((card_type, seq))
		return rt_list

	def pick_random_seq(self, cards):
		seq_list = self.create_combo_list(cards)
		p = len(seq_list)
		rand = random.randint(0, p-1)
		return seq_list[rand]

	def draw(self, pre_type, pre_seq, cards):
		rt_card_type, rt_seq = None, None
		if not pre_type:
			rt_card_type, rt_seq =  self.pick_random_seq(cards)
		else:
			combo_dict = self.create_combos(cards)
			candidates = []
			for seq in combo_dict[pre_type]:
				candidates.append((pre_type, seq))
			for seq in combo_dict['bomb']:
				candidates.append(('bomb', seq))
			for seq in combo_dict['rocket']:
				candidates.append(('rocket', seq))
			for card_type,seq in candidates:
				if self.compare(pre_type, pre_seq, card_type, pre_seq):
					rt_card_type = card_type
					rt_seq = seq
					break
		played = self.remove_from_card(cards, rt_seq)
		return rt_card_type, rt_seq, played

	def remove_from_card(self, cards, seq):
		removed = []
		counter = collections.Counter(seq)
		p = 0
		while p < len(cards):
			symbol = cards[p].symbol
			if symbol in counter and counter[symbol] > 0:
				counter[symbol] -= 1
				removed.append(cards.pop(p))
			else:
				p+=1
		return removed

	def compare(self, type1, seq1, type2, seq2):
		"""return true if seq2 is bigger than seq1."""
		val1 = self.getvalue(type1, seq1)
		val2 = self.getvalue(type2,seq2)
		if type2 == 'rocket':
			return True
		elif type2 == 'bomb':
			if type1 == 'bomb':
				return val2>val1
			else:
				return True
		else:
			if type2 == type1:
				return val2>val1
			else:
				return False

	def getvalue(self, seq_type, seq):
		"""Jay Chow Algorithm.
		333A < 4443 so we should not count the bias"""
		if seq_type == 'rocket':
			return 100000
		elif seq_type == 'bomb':
			val = self.value_map[seq[0]]
			return val*100
		else:
			counter = collections.Counter(seq)
			#{('a':3, 'b':2)}
			#（'a':3)
			# 3
			most_common = counter.most_common(1)[0][1]
			total_val = 0
			for letter in seq:
				if counter[letter] == most_common:
					total_val += self.value_map[letter]
			return total_val


if __name__ == '__main__':
	cards = [c(1,1), c(2,1),c(3,1),c(3,2),c(4,1),c(5,1),c(6,1),c(7,1)]
	rule = DDZRule()
	removed, cards = rule.remove_from_card(cards, '34567')
	print([str(c) for c in removed])
	print([str(c) for c in cards])