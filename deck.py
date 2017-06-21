#!/usr/env python3
# -*- coding:utf-8 -*-
#deck.py - a group of classes for working with playing card decks.
import copy
import random as r
random = r.SystemRandom()


suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values_ace_low = copy.deepcopy(values)
values_ace_low.insert(0, values_ace_low.pop())
values = tuple(values)
values_ace_low = tuple(values_ace_low)
