#!/usr/env python3
# -*- coding:utf-8 -*-
#blackjack.py - A more complicated example using the deck module
from deck import Deck
import sys


class Player():
def __init__(self, deck, playerName):
	self.deck = deck
	self.name = playerName
	self.facedown = None
	self.cards = []

