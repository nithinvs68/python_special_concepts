from queue import Queue


olympics=Queue(5)
# print(olympics)
print(olympics.empty())#True
olympics.put('United states(USA)')
olympics.put('Grate britin(GBR)')
print(olympics)
print(olympics.empty())#False  check wheather queue is empty
# print(len(olympics))
print(olympics.full())# check queue is full or not
print(olympics.qsize())#loaded elements output:2
olympics.put('china')
olympics.put('India')
olympics.put('Russia')
print(olympics.full()) #True
print(olympics.qsize()) #output:2
olympics.get()
print(olympics.qsize())#4
olympics.put('paki')
print(olympics.qsize())
olympics.dqueue()

'''Defining user queue'''

class MyQueue:
    def __init__(self):
        '''create a new queue'''
        self.item=[]

    def is_empty(self):
        '''Return true if queue is empty'''
        return len(self.item)==0

    def enqueue(self,item):
        '''Add a new element to the end of queue'''
        self.item.append(item)


    def dqueue(self):
        '''remove element from the beginning of queue'''
        return self.item.pop(0)


    def size(self):
        return len(self.item)


    def peek(self):
        if self.is_empty():
            raise Exception("Nothing to peek")

        return self.item[0]


sport=MyQueue()
sport.enqueue('USA')
sport.enqueue('UK')
print(sport.item)
print(sport.peek())
print(sport.size())
sport.enqueue('India')
sport.enqueue('Paki')
print(sport.size())
sport.dqueue()
sport.dqueue()
print(sport.peek())
print(sport.size())
print(sport.item)

