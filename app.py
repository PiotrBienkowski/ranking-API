import lib

class Player:
    sum_of_points = 0
    max_result = 0
    password_hash = "X"
    def __init__(self, name, password):
        self.name = name
        self.password_hash = lib.password_hash(password)

tab = []
tab.append(Player("Krzys", 5123))
tab.append(Player("Jan", 1234))
tab.append(Player("Jacek", 7234))

