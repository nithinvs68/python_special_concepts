from abc import ABC,abstractmethod

class Team(ABC):
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    def behavior(self):
        print("They show complex expression and social nehaviour")


class Human(Team):
    def diet(self):
        # pass #, Will get error if no implementation for this function since it is abstract in base class
        print("Human are carnivorous")

    def walk(self):
        # pass ,Will get error if no implementation for this function since it is abstract in base class
        print("They are bipeds")

class Tt(Team):
    # , Will get error if no implementation for this function since it is abstract in base class
    def diet(self):
        pass
        # print("Human are carnivorous")

    def walk(self):
        # pass ,Will get error if no implementation for this function since it is abstract in base class
        print("They are bipeds")

nithin=Human()
print(nithin.diet())
print(nithin.walk())
print(nithin.behavior())
ab=Tt()
print((ab.diet()))
# print(nithin.diet())
# help(ABC)
