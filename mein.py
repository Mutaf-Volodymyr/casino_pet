from player import Player
from game import Game

persons = [
    Player('Vova', 100_000),
    Player('Lena', 100_000),
    Player('Nikita', 100_000),
    Player('Sveta', 100_000),
    Player('Sasha', 100_000),
    Player('Kiril', 100_000),
    Player('Andrey', 100_000),
]

# persons[0].all_bet = list(zip(range(0, 37), range(100, 137))) # testing

if __name__ == '__main__':
    game = Game(*persons)
    game.start()