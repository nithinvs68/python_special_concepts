class Part:
    def __init__(self):
        self.__parti=[]

    def add_part(self,name):
        self.__parti.append(name)

    def __len__(self):
        return len(self.__parti)

p=Part()
print(len(p))
p.add_part('nithin')
print(len(p))

print(list.__dict__)