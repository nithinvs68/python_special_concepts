class Add():
    def __init__(self,amount):
        self.__amount=amount

    def __add__(self,other):
        return self.__amount + other.__amount

class Sub:

    def __init__(self, amount):
        self.__amount = amount

    def __sub__(self, other):
        return self.__amount - other.__amount
        #return self.__amount * other.__amount output will be multiplications

class Mul:

    def __init__(self, amount):
        self.__amount = amount

    def __mul__(self, other):
        if type(other)==int or type(other)==float:
            return self.__amount * other.__amount
        else:
            raise ValueError('Can only multipy by int or float')
    #float.__mul__(1.0*2.5) success
    #float.__mul__(1,2.1) Error

class Floardiv:
    def __init__(self,num):
        self.__num=num

    def __floordiv__(self, other):
        return self.__num//other.__num




s1=Add(1000)
s2=Add(2000)
print(s1+s2)  #s1.__add__(s2)

su1=Sub(10)
su2=Sub(9)
print(su1-su2)

m1=Mul(9)
m2=Mul(8)
print(m1*m2)
#both parameters should be int or float, if m1 is int then m2 should also be int
#print(m1*10)#error

f1=Floardiv(9)
f2=Floardiv(5)
print(f1//f2)