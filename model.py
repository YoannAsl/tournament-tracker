from faker import Faker

fake = Faker()


class Player:
    def __init__(self, last_name: str, first_name: str, birthdate: str, gender: str, ranking: int):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birthdate} {self.gender} {self.ranking}"

    def __repr__(self):
        return str(self)


# p1 = Player(fake.first_name(), fake.last_name(), fake.date_of_birth(), "Male", 1)
# print(p1)


class Tournament:
    def __init__(
        self, name: str, place: str, date: str, rounds: int, players, time: int, description: str, turns: int = 4
    ):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.time = time
        self.description = description
        self.turns = turns


class Match:
    def __init__(self, player1, player2, player1_res, player2_res):
        pass
