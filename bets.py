from abc import ABC, abstractmethod
from datetime import datetime


class MistakeBet(Exception):
    pass


class Bet(ABC):
    def __init__(self, player: str, money: int, bet):
        self.min_bet = 100
        self.max_bet = 10_000
        self.player: str = player.title()
        self.money: int = self.__is_valid_money(money)
        self.bet = bet

    # @abstractmethod
    # def __is_valid_bet(self, bet):
    #     pass

    @abstractmethod
    def check_a_win(self, value: tuple) -> bool:
        pass

    def __is_valid_money(self, money):
        if self.max_bet < money or money < self.min_bet:
            raise MistakeBet(f'Mistake bet: <{money}>. Bet mast be {self.min_bet} to {self.max_bet}')
        return money

    def make_loging(self):
        with open(f'log.txt', 'a') as log:
            log.write(f'{datetime.now()}: {str(self)}\n')

    def __str__(self):
        return f'{self.player} bet {self.money} on {self.bet}'

    def __repr__(self):
        return f'{self.player} - {self.money} - {self.bet}'


class DirectBet(Bet):
    def __init__(self, player, money, bet):
        super().__init__(player, money, bet)
        self.bet: int = self.__is_valid_bet(bet)

    def __is_valid_bet(self, bet: int):
        if bet not in range(0, 37):
            raise MistakeBet(f'Invalid bet number {bet}. Only 0-36')
        return bet

    def check_a_win(self, value: tuple) -> bool:
        if value[0] == self.bet:
            return True
        return False


class EvenOrOddBet(Bet):
    def __init__(self, player, money, bet):
        super().__init__(player, money, bet)
        self.bet = self.__is_valid_bet(bet)

    def __is_valid_bet(self, bet: str):
        if bet not in ('even', 'odd'):
            raise MistakeBet(f'Invalid names of bet {bet}. Only <even> or <odd>.')
        return bet

    def check_a_win(self, value: tuple) -> bool:
        if value[0] == 0:
            return False
        elif ('even', 'odd')[value[0] % 2] == self.bet:
            return True
        return False


class BlackOrRedBet(Bet):
    def __init__(self, player, money, bet):
        super().__init__(player, money, bet)
        self.bet: str = self.__is_valid_bet(bet)

    def __is_valid_bet(self, bet: str):
        if bet not in ('black', 'red'):
            raise MistakeBet(f'Invalid color {bet}. Only <black> or <red>')
        return bet

    def check_a_win(self, value: tuple) -> bool:
        return value[1] == self.bet


class MoreOrLess(Bet):
    def __init__(self, player, money, bet):
        super().__init__(player, money, bet)
        self.bet = self.__is_valid_bet(bet)

    def __is_valid_bet(self, bet: str):
        if bet not in ('more', 'less'):
            raise MistakeBet(f'Invalid names of bet {bet}. Only <more> or <less>')
        return bet

    def check_a_win(self, value: tuple) -> bool:
        if value[0] == 0:
            return False
        elif ('less', 'more')[value[0] > 18] == self.bet:
            return True
        return False



############ TESTING ############
# win = (20, 'red')
# bet1 = DirectBet('anton', 1000, 0)
# bet2 = EvenOrOddBet('anton', 1000, 'even')
# bet3 = BlackOrRedBet('anton', 1000, 'red')
# bet4 = MoreOrLess('anton', 1000, 'more')
#
#
# print(bet1)
# print(bet1.check_a_win(win))
# print(bet2)
# print(bet2.check_a_win(win))
# print(bet3)
# print(bet3.check_a_win(win))
# print(bet4)
# print(bet4.check_a_win(win))




