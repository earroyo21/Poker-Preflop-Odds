'''
Created on Mar 13, 2022

@author: ethanarroyo
'''
from collections import defaultdict
from deck import Card

def print_hand(cards):
    for i in cards:
        print(i, end = ' ')
    print()

def check_flush(cards):
    suit_dict = defaultdict(list)
    for card in cards:
        suit_dict[card.get_suit()].append(card)
        
    for suited_cards in suit_dict.values():
        if len(suited_cards) >= 5:
            return (sorted(suited_cards, reverse=True)[:5], 5)

def check_straight(cards): # ACCOUNT FOR ACE LOW CASE
    sorted_cards = sorted(cards, reverse=True)
    ace_check = False
    # for card in list(sorted_cards):
    #     if card.get_value() < 14:
    #         break
    #     elif card.get_value() == 14:
    #         sorted_cards.append(Card(1, card.get_suit()))
    #         ace_check = True
        
    for c in range(len(sorted_cards)-4):
        for i in range(4):
            if sorted_cards[c+i].get_value() - sorted_cards[c+i+1].get_value() != 1:
                break
            if i == 3:
                return (sorted_cards[c:c+5], 4)
# (hi, ur cute and i think ur hot and attractive 
# very good eye candy 
# u should take off ur shirt again 
# i like when u do that 
# u should just never wear a shirt again 
# i like u better that way 
# i also especially like ur kisses and hugs and everything else ;)
# hehehe ur my cute little dinosaur who likes to eat my face for no reason 
# but it's okay i still love u don't tell anyone tho it's a secret 
# oh and u smell good as usual
# u also look a lil emo sometimes but ur still cute 

def check_pairs(cards):
    match_dict = defaultdict(list)
    sorted_cards = sorted(cards, reverse=True)
    for card in sorted_cards:
        match_dict[card.get_value()].append(card)
    
    four_match = []
    three_match = []
    two_match = []
    
    
    for matches in match_dict.values():
        match_size = len(matches)
        if match_size == 4:
            four_match.append(matches)
        elif match_size == 3:
            three_match.append(matches)
        elif match_size == 2:
            two_match.append(matches)
        # else:
        #     unpaired.append(matches[0])
            
    # base = None
    # needed_kickers = 0
    if four_match:
        needed_kickers = 1
        base = four_match[0]
        hand_rank = 7
        # hand_rank = 'FOUR KIND'
    
    elif three_match and two_match:
        needed_kickers = 0
        base = [*three_match[0], *two_match[0]]
        hand_rank = 6
        # hand_rank = 'FULL HOUSE'
    
    elif three_match:
        needed_kickers = 2
        base = three_match[0]
        hand_rank = 3
        # hand_rank = 'THREE KIND'
    
    elif two_match and len(two_match) >= 2:
        needed_kickers = 1
        base = [*two_match[0], *two_match[1]]
        hand_rank = 2
        # hand_rank = 'TWO PAIR'
    
    elif two_match:
        needed_kickers = 3
        base = two_match[0]
        hand_rank = 1
        # hand_rank = 'PAIR'
    
    else:
        needed_kickers = 5
        base = []
        hand_rank = 0
        # hand_rank = 'HIGH CARD'

    while needed_kickers > 0:
        kicker = sorted_cards.pop(0)
        if not kicker in base:
            base.append(kicker)
            needed_kickers -= 1
    return (base, hand_rank)

if __name__ == '__main__':
    cards = [Card(14, 's'), Card(12,'d')] + [Card(5, 'd'), Card(4, 'c'), Card(3, 'h'), Card(2, 'd'), Card(5, 'c')]
    hand = check_straight(cards)
    print_hand(hand[0])
    print(hand[1])




