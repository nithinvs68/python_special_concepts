def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def maths(func):
    op=func(6,5)
    return op


print(maths(add))
print(maths(sub))