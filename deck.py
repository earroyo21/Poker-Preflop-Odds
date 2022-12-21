'''
Created on Mar 11, 2022

@author: ethanarroyo
'''
import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return str(self.value) + self.suit
    
    def __lt__(self, right):
        if isinstance(right, Card):
            return self.get_value() < right.get_value()
        else:
            raise TypeError
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit

class Deck:
    def __init__(self):
        _suits = ('c', 'd', 'h', 's')
        self.cards = [Card(value, suit) for value in range(2,15) for suit in _suits]
    
    def __str__(self):
        deck_str = ''
        for card in self.cards:
            deck_str += str(card) + ' '
        return deck_str
    
    def __len__(self):
        return len(self.cards)
    
    def get_card(self, value=None, suit=None):
        if value == None and suit == None:
            return self.cards.pop(random.randint(0, len(self.cards)-1))
        
        elif value != None and suit != None:
            for c in range(len(self.cards)):
                if self.cards[c].get_value() == value and self.cards[c].get_suit() == suit:
                    return self.cards.pop(c)
        
        else:
            raise AttributeError
    
    def get_cards(self, n: int):
        for _ in range(n):
            if self.cards:
                return self.cards.pop(random.randint(0, len(self.cards)-1))
    
    def get_sorted_cards(self, r=False):
        return sorted(self.cards)
    
    def collect_card(self, card):
        self.cards.append(card)
    
# card_2s = Card(2, 's')
# print(card_2s)
# deck = Deck()
# print(deck)
# for card in deck.get_sorted_cards():
#     print(card)