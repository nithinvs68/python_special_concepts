class Compitation():
    __raise_count=1.04

    def __init__(self,name,prize):
        self.__name=name
        self.__prize=prize

    def raise_prise(self):  #instance method
        self.__prize=self.__prize*self.__raise_count

    def print_details(self):  #instance method
        print("Name: {},prize: {}".format(self.__name,self.__prize))


    @classmethod
    def get_raise_count(cls): #class method, state on class not instant or object
        return cls.__raise_count

    @classmethod
    def set_raise_count(cls,count): #class method
        cls.__raise_count=count

    @classmethod
    def from_str(cls,com_str_prize):
        name,prize=com_str_prize.split('-')
        return cls(name,prize) #instance of a class


sprint=Compitation('Sprint',10000)
print(sprint.get_raise_count())
sprint.set_raise_count(1.06)
print(sprint.get_raise_count())
print(Compitation.get_raise_count())

swmming_str='Swimming-8000'
name,prize=swmming_str.split('-')
swimming=Compitation(name,prize)
print(swimming.print_details())


archery_str='Archery-8000'
arch=Compitation.from_str(archery_str)
print(arch.print_details())


#Static methods
class Rectangle:

    def area(x,y):    #no self does not belong to class itself
        return x*y


Rectangle.area=staticmethod(Rectangle.area)
print('area of the rectangle is :',Rectangle.area(15,16))


class Rectange2:
    @staticmethod
    def area(x,y):
        return x*y

rec=Rectange2()
print(rec.area(4,5))


