class Wrestler:
     def __init__(self,name,age):
         self.__name=name
         self.__age=age

     @property
     def name(self):
         print('Name getter method called')
         return self.__name

     @name.setter
     def name(self,value):
         print('Name setter method called')
         self.__name=value

     @name.deleter
     def name(self):
         print('Name deleter method called')
         del self.__name

     @property
     def age(self):
         print('age getter method called')
         return self.__age

     @age.setter
     def age(self,value):
         print('age setter method called')
         self.__age=value


     @age.deleter
     def age(self):
         print('Age deleter method called')
         del self.__age



w=Wrestler('Adam',45)
print(w.name)#call getter method
print(w.age)#call getter method
w.name='Nithin'#call setter method
w.age=23#call setter method
print(w.name)#call getter method
print(w.age)#call getter method
del w.name #call deletor method
del w.age #call deletor method
# print(w.name)# Attribute Error
# print(w.age)# Attribute Error
