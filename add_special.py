class Savings():
    def __init__(self,amount):
        self.__amount=amount

    def __add__(self,other):
        return self.__amount + other.__amount

s1=Savings(1000)
s2=Savings(2000)
print(s1+s2)  #s1.__add__(s2)