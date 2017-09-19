from card import Cards
from desk import Table
from player import AiPlayer, Player
from event import DDZEvent

def main():
	table = Table()
	table.add_cards(Cards())
	table.add_player(AiPlayer())
	table.add_player(AiPlayer())
	table.add_player(Player())
	table.add_event(DDZEvent())
	table.start()



if __name__ == '__main__':
	main()
