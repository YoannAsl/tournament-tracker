from faker import Faker

fake = Faker()


class Tournament:
    def __init__(self, name, place, date, rounds, players, time, description, turns=4):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.time = time
        self.description = description
        self.turns = turns


class Player:
    def __init__(self, last_name, first_name, birthdate, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking


class Match:
    def __init__(self, player1, player2, player1_res, player2_res):
        pass
