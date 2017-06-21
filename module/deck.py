#!/usr/env python3
# -*- coding:utf-8 -*-
#deck.py - a group of classes for working with playing card decks.
import copy
import random as r
random = r.SystemRandom()


suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values_ace_low = copy.deepcopy(values)
values_ace_low.insert(0, values_ace_low.pop())
values = tuple(values)
values_ace_low = tuple(values_ace_low)


class Card():
	def __init__(self, value, suit, valueset=values):
		self.values = valueset
		self.suit = suit
		self.value = value
		self.cardId = self.values.index(value) + (suits.index(suit) * 52//4)
		self.fullName = "%s of %s" % (self.value, self.suit)
		self.__int = self.values.index(value) + 1
	def __int__(self):
		return self.__int
	def __str__(self):
		return self.fullName
	def __eq__(self, other):
		return (int(self) == int(other))
	def __le__(self, other):
		return (int(self) <= int(other))
	def __lt__(self, other):
		return (int(self) < int(other))
	def __ge__(self, other):
		return (int(self) >= int(other))
	def __gt__(self, other):
		return (int(self) > int(other))
	def __ne__(self, other):
		return (int(self) != int(other))


class Deck():
	def __init__(self, ace_high):
		if ace_high:
			self.values = values
		else:
			self.values = values_ace_low
		self.cards = []
		for suit in suits:
			for value in values:
				self.cards.append(Card(value, suit, self.values))
		self.deck = copy.copy(self.cards)
		random.shuffle(self.deck)
	def shuffle(self, dont_shuffle_in):
		self.deck = copy.copy(self.cards)
		if dont_shuffle_in:
			for card in dont_shuffle_in:
				del(self.deck[self.deck.index(card)])
		random.shuffle(self.deck)
	def draw(self, reshuffle=False):
		if len(self.deck) == 0:
			if reshuffle:
				self.shuffle()
			else:
				return None
		return self.deck.pop()
	def drawhand(self, no, reshuffle=False):
		hand = []
		for x in range(no):
			hand.append(self.draw(reshuffle))
		return hand


class PartialDeck(Deck):
	def __init__(self, cards):
		self.deck = copy.copy(cards)
		self.cards = []
	def add_cards(self, cards):
		self.cards = cards + self.cards
	def __bool__(self):
		return (len(self.cards) > 0 or len(self.deck) > 0)
	def __int__(self):
		return len(self.cards)
	def shuffle(self):
		self.deck = copy.copy(self.cards)
		random.shuffle(self.deck)
		del(self.cards)
		self.cards = []
