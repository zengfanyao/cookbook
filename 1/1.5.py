import heapq

class PriorityQueue:

    def __index__(self):
        self.queue=[]
        self._index=0

    def push(self,item,priority):
        heapq.heappush(self.queue,(-priority,self._index,item))
        self._index+=1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class Item:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return "Item{{!r}}".format(self.name)

q=PriorityQueue()

q.push(Item('Bat'),2)
q.push(Item('foo'),4)
q.push(Item('grok'),1)

a=Item('a')
b=Item('b')
print(a>b)