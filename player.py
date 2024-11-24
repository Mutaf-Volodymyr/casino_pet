
class Player:
    def __init__(self, name: str, money: float):
        self.name = name.title()
        self.money = money
        self.all_bet = []

    def __str__(self):
        return self.name

    def make_bet(self):
        while True:
            bet = input(f'{self.name}, make a bet! <num> <cash>, or pass:  ')
            if bet == 'pass':
                break
            bet = tuple(map(int, bet.split()))
            if self.is_valid_bet(bet):
                self.all_bet.append(bet)
                self.money -= bet[1]

            print(self.all_bet)
            print(self.money)

    def is_valid_bet(self, bet: tuple) -> bool:
        num, cash = bet
        if not (36 >= num >= 0):
            print('Num is not valid')
            return False
        if cash <= 0:
            print('Cash is not valid')
            return False
        if cash > self.money:
            print('Not enough money')
            return False
        return True

    def clin_all_batt(self):
        self.all_bet = []
