import json
import collections
from card import DDZCard as c

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



def find_combos(cards):
	with open('rule.json', 'r') as f:
		rules = json.load(f)
	d = collections.defaultdict(int)
	ans = collections.defaultdict(list)
	for card in cards:
		d[card.symbol] += 1
	for card_type, seqs in rules.iteritems():
		for seq in seqs:
			counter = collections.Counter(seq)
			include = True
			for symbol, count in counter.iteritems():
				if symbol not in d or d[symbol] < counter[symbol]:
					include = False
					break
			if include:
				ans[card_type].append(seq)
	return ans



cards = [c(1,1), c(2,1),c(3,1),c(4,1),c(5,1),c(6,1),c(7,1)]
ans = find_combos(cards)
print ans