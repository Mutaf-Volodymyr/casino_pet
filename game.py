
from random import randint

class Game:
    def __init__(self, *player) :
        self.direct_bet = 36
        self.players = player
        self.win_number = None
        self.game_over = False

    def start(self):
        while not self.game_over:
            for player in self.players:
                player.make_bet()
            self.win_number = randint(0, 36)
            print(f'Winner num: {self.win_number}')
            for player in self.players:
                self.search_winner(player)
                print(f'Balance {player} is {player.money}$')

    def search_winner(self, player):
        for num, summ in player.all_bet:
            if self.win_number == num:
                self.make_payout(summ, player)
        player.clin_all_batt()

    def make_payout(self,summ, player):
        player.money += summ * self.direct_bet
        print(f'Player: {player} is winner!!!')









