from pymongo import MongoClient, WriteConcern, ReadPreference
from pymongo.errors import PyMongoError
from pymongo.synchronous.client_session import ClientSession
import os
import dotenv
from pathlib import Path
from random import choice
from bets import *


class Game:
    def __init__(self, *players) :
        self.__table = {
            36: 'red', 33: 'black', 30: 'red', 27: 'red', 24: 'black', 21: 'red', 18: 'red', 15: 'black', 12: 'red', 9: 'red', 6: 'black', 3: 'red',
            35: 'black', 32: 'red', 29: 'black', 26: 'black', 23: 'red', 20: 'black', 17: 'black', 14: 'red', 11: 'black', 8: 'black', 5: 'red', 2: 'black',
            34: 'red', 31: 'black', 28: 'black', 25: 'red', 22: 'black', 19: 'red', 16: 'red', 13: 'black', 10: 'black', 7: 'red', 4: 'black', 1: 'red',
            0: 'green'
        }
        self.__players: set = set(players)
        self.__win_number = None
        self.game_over = False

    def __choice_winner_number(self):
        self.win_number = choice(self.__table)
        with open('log.txt', 'a') as f:
            f.write(f'{datetime.now()}: winner nummer is {self.__win_number}\n')

    def show_all_players(self):
        print(self.__players)

    def __search_winners(self, bets: list[Bet]):
        for bet in bets:
            if bet.check_a_win(self.win_number):
                pass

    def __make_transaction(self, sender, recipient, amount):
        dotenv.load_dotenv(Path('.env'))
        client = MongoClient(
            os.environ.get('MONGO_URI'),
            tls=True,  # Использование TLS (SSL)
            tlsAllowInvalidCertificates=True
        )

        db = client.get_database(
            name=os.environ.get('TARGET_DB'),
            write_concern=WriteConcern(w="majority")
        )  # use db

        collection = db.get_collection(
            name=os.environ.get('TARGET_COLLECTION'),
            write_concern=WriteConcern(w="majority"),
            read_preference=ReadPreference.PRIMARY
        )

        session: ClientSession = client.start_session()

        with session.start_transaction():
            try:
                collection.update_one(
                    {"name": sender},
                    {"$inc": {"money": -amount}},
                    session=session
                )

                name_sender = collection.find_one(
                    {"name": sender},
                    session=session
                )

                if name_sender['money'] < 0:
                    raise ValueError("Balance cannot be negative")

                collection.update_one(
                    {"name": recipient},
                    {"$inc": {"money": amount}},
                    session=session
                )

            except (PyMongoError, ValueError) as e:
                print(f"ERROR, transaction will be aborted: [{e}]")
                session.abort_transaction()
            else:
                session.commit_transaction()
            finally:
                session.end_session()
                client.close()


    def start(self):
        while not self.game_over:
            pass











