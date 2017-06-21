#!/usr/env python3
# -*- coding:utf-8 -*-
#An example for the deck module
from deck import Deck, PartialDeck
def main():
	deck = Deck(False)
	hand = 26
	player_draw = deck.drawhand(hand)
	comp_draw = deck.drawhand(hand)
	playerDeck = PartialDeck(player_draw)
	compDeck = PartialDeck(comp_draw)
	cards = []
	while playerDeck and compDeck:
		c = input('Press [Enter] to continue, or enter anything else to quit.')
		if len(c) > 0:
			break
		pflip = playerDeck.draw(True)
		cflip = compDeck.draw(True)
		cards += [pflip, cflip]
		if int(pflip) == 1 or int(cflip) == 1:
			message = "Ace! Automatic tie!"
		elif pflip > cflip:
			message = "You win this round!"
			playerDeck.add_cards(cards)
			cards = []
		elif pflip < cflip:
			message = "The computer wins this round."
			compDeck.add_cards(cards)
			cards = []
		else:
			message = "Tie"
		print("You got the %s." % (pflip))
		print("The computer got the %s." % (cflip))
		print(message)
		print("You have %d cards left." % (int(playerDeck)))
		print("The computer has %d cards left." % (int(compDeck)))
		print("The stake of the next round is %d cards." % (len(cards) + 2))
	c = input('Would you like to play again?(y/n)')
	if c.lower().startswith('y'):
		main()
	else:
		c = input('Are you sure?(y/n)')
		if c.lower().startswith('y'):
			return
		else:
			main()


if __name__ == "__main__":
	main()
