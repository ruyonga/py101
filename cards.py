#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:44:41 2023

@author: ruyonga
"""


class Card:
    
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    ranks = ["narfs", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack","Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.ranks[self.rank]} of {self.suits[self.suit]}"
    
    def cmp(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        
    
class Deck:
    
    def __init__(self):
        self.cards = []
        
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
                

class Hand(Deck):
    
    def __init__(self, name=""):
        self.cards = []
        self.name = name