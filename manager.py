from card import Cards
from desk import Table
from player import AiPlayer, Player, PlayerBase
from event import DDZEvent
from rule import DDZRule

def main():
	PlayerBase.add_rule(DDZRule())
	table = Table()
	table.add_cards(Cards())
	table.add_player(AiPlayer())
	table.add_player(AiPlayer())
	table.add_player(Player())
	table.add_event(DDZEvent())
	table.start()



if __name__ == '__main__':
	main()
