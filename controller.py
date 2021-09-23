from model import Player
from faker import Faker
from tinydb import TinyDB

fake = Faker()
db = TinyDB("db.json")

serialized_players = []
players_table = db.table("players")
players_table.truncate()

# serialized_players = players_table.all()


def init():
    for i in range(9):
        player = Player(fake.first_name(), fake.last_name(), str(fake.date_of_birth()), "Male", i)
        serialized_player = {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birthdate": str(player.birthdate),
            "gender": player.gender,
            "rank": player.ranking,
        }
        serialized_players.append(serialized_player)
    players_table.insert_multiple(serialized_players)


init()
