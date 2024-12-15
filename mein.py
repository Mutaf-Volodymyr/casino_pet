from game import Game

persons = ['Elena', 'Vova']


# persons[0].all_bet = list(zip(range(0, 37), range(100, 137)))

if __name__ == '__main__':
    game = Game(*persons)
    game.start()
