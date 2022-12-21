'''
Created on Mar 11, 2022

@author: ethanarroyo
'''
from deck import Deck
from player import Player

NAMES = ['Jimmy', 'Johnny', 'Timmy', 'Tommy']
HANDS = ['HIGH CARD', 'ONE PAIR', 'TWO PAIR', 'THREE OF A KIND',
         'STRAIGHT', 'FLUSH', 'FULL HOUSE', 'FOUR OF A KIND', 'STRAIGHT FLUSH']


class Game:
    def __init__(self, player_count=3, starting_chips=100, preflop_simulation=False):
        self.deck = Deck()
        self.board = []
        self.players = []
        for i in range(player_count):
            self.players.append(Player(starting_chips, name=NAMES[i]))

    def __str__(self):
        game_str = self.board_str() + '\n\n' + self.players_str()
        return game_str

    def deal_board(self):
        self.board.append(self.deck.get_card())

    def deal_players(self):
        for _ in range(2):
            for player in self.players:
                if len(player.get_hand()) < 2:
                    player.receive_card(self.deck.get_card())

    def deal_preflop(self):
        for _ in range(3):
            self.deal_board()

    def clear_board(self):
        for _ in range(len(self.board)):
            self.deck.collect_card(self.board.pop(0))

    def clear_players(self):
        for player in self.players:
            card1, card2 = player.return_cards()
            self.deck.collect_card(card1)
            self.deck.collect_card(card2)

    def clear_hand(self):
        self.clear_board()
        self.clear_players()

    def board_str(self):
        board_str = 'Board: '
        for card in self.board:
            board_str += str(card) + ' '
        return board_str

    def players_str(self):
        player_str = ''
        for player in self.players:
            player_str += str(player) + '\n\n'
        return player_str

    def evaluate_hands(self):
        for p in self.players:
            p.evaluate_hand(self.board)

    def winner(self):
        winner = self.compare(self.players[0], self.players[1])
        for i in range(2, len(self.players)):
            if type(winner) == list:
                temp = self.compare(winner[0], self.players[i])
                if type(temp) == list:
                    winner.append(temp[1])
                elif temp not in winner:
                    winner = temp

            else:
                temp = self.compare(winner, self.players[i])
                winner = temp
        return winner

    @staticmethod
    def compare(p1: Player, p2: Player):
        if p1.hand_rank > p2.hand_rank:
            return p1
        elif p1.hand_rank < p2.hand_rank:
            return p2
        else:
            # print('Tie:')
            # print_hand(p1.hand)
            # print_hand(p2.hand)
            for i in range(len(p1.hand)):
                if p1.hand[i] > p2.hand[i]:
                    # print(p1.name + ' won')
                    return p1
                elif p1.hand[i] < p2.hand[i]:
                    # print(p2.name + ' won')
                    return p2
            # print('Same Hands')
            return [p1, p2]

    def set_player_hand(self, player_name, card1, card2):
        c1value, c1suit = card1
        c2value, c2suit = card2

        for player in self.players:
            if player.get_name() == player_name:
                player.receive_card(self.deck.get_card(c1value, c1suit))
                player.receive_card(self.deck.get_card(c2value, c2suit))
                break


def print_hand(cards):
    for i in cards:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    # game = Game()
    # game.deal_players()
    # print(game.players_str())
    # for i in range(5):
    #     game.deal_board()
    # print(game.board_str())
    # print()
    # game.evaluate_hands()
    # print(game.players[0].name)
    # print_hand(game.players[0].hand)
    # print(game.players[0].hand_rank)
    # print(game.players[1].name)
    # print_hand(game.players[1].hand)
    # print(game.players[1].hand_rank)
    # print(game.players[2].name)
    # print_hand(game.players[2].hand)
    # print(game.players[2].hand_rank)
    # print()
    # print('WINNER:')
    #
    # winner = game.winner()
    # if type(winner) == list:
    #     for p in winner:
    #         print(p)
    # else:
    #     print(winner)

    # for i in range(10000):
    #     game = Game()
    #     game.deal_players()
    #     print(game.players_str())
    #     for i in range(5):
    #         game.deal_board()
    #     print(game.board_str())
    #     print()
    #     game.evaluate_hands()
    #     print(game.players[0].name)
    #     print_hand(game.players[0].hand)
    #     print(game.players[0].hand_rank)
    #     print(game.players[1].name)
    #     print_hand(game.players[1].hand)
    #     print(game.players[1].hand_rank)
    #     print(game.players[2].name)
    #     print_hand(game.players[2].hand)
    #     print(game.players[2].hand_rank)
    #     print()
    #     print('WINNER:')
    #     winner = game.winner()
    #     if type(winner) == list:
    #         for p in winner:
    #             print(p)
    #     else:
    #         print(winner)
    #     print()
    #     print('================================')
    #     print()

    game = Game(player_count=2)
    p_dict = dict()
    for p in game.players:
        p_dict[p.name] = 0
        p_dict[p.name+' Tie'] = 0

    accuracy = 20000
    for i in range(accuracy):
        game = Game(player_count=2)
        game.set_player_hand('Jimmy', (10, 'h'), (9, 'c'))
        game.set_player_hand('Johnny', (11, 'd'), (10, 'd'))
        game.deal_players()
        for i in range(5):
            game.deal_board()

        game.evaluate_hands()
        winner = game.winner()

        if type(winner) == list:
            # print(game.players_str())
            # print(game.board_str())
            # print()
            # print(HANDS[winner[0].hand_rank])
            # print_hand(winner[0].hand)
            # print('WINNERS:')

            for p in winner:
                p_dict[p.name+' Tie'] += 1

            #     print(p)
            # print()
            # print('================================')
            # print()
        else:
            # if True:
            #     print(game.players_str())
            #     print(game.board_str())
            #     print()
            #     for player in game.players:
            #         print(player.name + ': ' +
            #               HANDS[player.hand_rank], end=' ')
            #         # print_hand(player.hand)
            #     print()
            #     print('================================')
            #     print()
            p_dict[winner.name] += 1

    # print(p_dict)

    for player in game.players:
        name = player.get_name()
        print(name + ':')
        print(str(p_dict[name]/accuracy * 100) + '%')
        print(str(p_dict[name + ' Tie']/accuracy * 100) + '%')
        print()
