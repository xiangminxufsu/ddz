from card import Cards
from desk import Table
from player import Player


def main():
	table = Table()
	table.add_cards(Cards())
	table.add_player(Player())
	table.add_player(Player())
	table.add_player(Player())
	table.distribute_card()
	for p in table.players:
		p.print_cards()
		print



if __name__ == '__main__':
	main()
