class BusinessPerson():
    def __init__(self, name):
        self.name = name
        self.money = 1000
        print("Person name : " + self.name.title())
        print("Person money : $" + str(self.money).title())
