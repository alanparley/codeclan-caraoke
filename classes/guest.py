class Guest:

    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash

    def guest_can_pay(self, entry_cost):
        self.cash -= entry_cost
