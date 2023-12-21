class Compitation:
    def __init__(self,name,price,country):
        self.__name=name
        self.__price=price
        self.__country=country

    def __repr__(self):
        return "Compitation: {} held in {},price: {}".format(self.__name,self.__country,self.__price)

    def get_cou(self):
        return '{} {}'.format(self.__name,self.__country)

    def __str__(self):
        return '{}  {}'.format(self.get_cou(),self.__price)


rowing=Compitation('Rowing',10000,'uk')
# print(rowing)
print(repr(rowing))
print(rowing.__repr__())
print(str(rowing))



