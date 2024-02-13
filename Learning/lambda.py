st='abcde'
print(st[::-1])
li=[1,1,3,4,5,5,6]
k=set(li)
print(list(k))
ll=list(k)
ll.sort()
print(ll[-2])

class A():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b


class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)

g=B(1,2)
print(g.add())