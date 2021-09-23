from tinydb import TinyDB

db = TinyDB("db.json")

players_table = db.table("players")
players_table.truncate()
players_table.insert_multiple(serialized_players)

serialized_players = players_table.all()
