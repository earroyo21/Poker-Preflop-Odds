'''
Created on Mar 11, 2022

@author: ethanarroyo
'''
from handeval import check_flush, check_straight, check_pairs

class Player:
    def __init__(self, chips, name='Player'):
        self.name = name
        self.chips = chips
        self.cards = []
        self.hand = None
        self.hand_rank = None
    
    def __str__(self):
        if self.cards:
            return f'{self.name}:\nChips: {self.chips}    Hand: {str(self.cards[0])},{str(self.cards[1])}'
        
        else:
            return f'{self.name}:\nChips: {self.chips}    Hand: EMPTY'
    
    def receive_card(self, card):
        self.cards.append(card)
    
    def return_cards(self):
        return (self.cards.pop(), self.cards.pop())
    
    def get_hand(self):
        return self.cards
    
    def get_name(self):
        return self.name
    
    def evaluate_hand(self, board):
        cards = self.cards + board
        original = list(cards)
        flush = check_flush(cards)
        straight = check_straight(cards)
        
        if flush and straight:
            self.hand, self.hand_rank = (flush[0], 8)
        
        elif flush:
            self.hand, self.hand_rank = flush
        
        elif straight:
            self.hand, self.hand_rank = straight
            
        else:
            self.hand, self.hand_rank = check_pairs(cards)
        
        
        
        
        
        
        
        
        