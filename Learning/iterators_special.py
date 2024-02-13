class Part:
    def __init__(self):
        self.__pa=[]
        self.__index=0

    def add_pa(self,name):
        self.__pa.append(name)

    def __len__(self):
        return len(self.__pa)

    def __iter__(self):
        self.__index=0
        return self

    def __next__(self):
        if self.__index==len(self.__pa):
            raise StopIteration
        p=self.__pa[self.__index]
        self.__index+=1

        return p

pa=Part()
pa.add_pa('sbhgj')
pa.add_pa('kfhoief')
pa.add_pa('dfdefg')
pa.add_pa('fdrg')

for p in pa:
    print(p,end=' ',)

pa.add_pa('wedff')
print('\n')
for i in pa:
    print(i,end=' ')

print('\n',iter(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
print(next(pa))
# print(next(pa)) Error stopiterator index out of range
