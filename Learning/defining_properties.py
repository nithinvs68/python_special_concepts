class Werstler(object):
    def __init__(self):
        self.__name=''

    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name


w1=Werstler()
w1.set_name('Nithin')
print(w1.get_name())
# print(w1.__name) Error
print(w1.__dict__)#no error output will be {'_Werstler__name': 'Nithin'}

class Werstler2(object):
    def __init__(self):
        self.__name=''

    def set_name(self,name):
        print('setter method')
        self.__name=name

    def get_name(self):
        print('getter method')
        return self.__name

    name=property(get_name,set_name)  #property(fget,fset,fdel,doc)

w=Werstler2()
w.name='King'  #setter method called
print(w.name)  #getter method called

class Werstler3(object):
    def __init__(self):
        self.__name=''

    def set_name(self,name):
        print('setter method')
        self.__name=name

    def get_name(self):
        print('getter method')
        return self.__name

    def del_name(self):
        print('delete method')
        del self.__name

    name = property(get_name, set_name,del_name)


w3=Werstler3()
w3.name='Losser'
print(w3.name)
del w3.name
# print(w3.name) #Attribute error if you access get after deletion