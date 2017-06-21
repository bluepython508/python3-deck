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

