def superReducedString(s):
    l=list(s)
    # while len(l)>2:
    # print(len(s))
    while True:
        for i in range(0,len(s)-1):
            print(i,l)
            a,b=l[i],l[i+1]
            if a==b:
                l.remove(a)
                l.remove(b)
                break
        else:
            break
    return "".join(l)


print(superReducedString('aashhtyyiotyrfguggg'))