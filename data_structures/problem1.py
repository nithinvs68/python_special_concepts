class LL():
    def __init__(self,a):
        self.a=a

class LK(LL):
    def __init__(self,a):
        super().__init__(a)


pp=LK('fef')
print(pp.a)
l1=["2",'3','5']
k="".join(l1)
print(list(k))
print("".join(l1))
# print(['even'for x in l1 if x%2==0])
# print([(x, y) if x != y and x > y else (0,0) for x in range(5) for y in range(5)])
# print([[x*y for y in range(4)] for x in range(3)])