from collections import deque

class Queue:
    def __init__(self):
        self.lisst = deque()

    def produce_binary(self,n):
        self.lisst.appendleft('1')
    
        for i in range(n):
            front=str(self.lisst[-1])
        
            self.lisst.appendleft(front+'0')
            
            self.lisst.appendleft(front+'1')
            print(self.lisst.pop())
            
            # i = i + 1

dharm =Queue()
dharm.produce_binary(10)
