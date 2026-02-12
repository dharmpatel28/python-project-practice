import time
import threading
from collections import deque

class Queue:
    def __init__(self):
        self.lisst = deque()

    print(f'5. execution start: {time.ctime()}')
    def place_order(self,orders):
        i = -1
        for element in orders.split(','):
            print(f'placing order for: {element}')
            self.lisst.appendleft(element)
            print(dharm.lisst[i])
            i = i - 1
        time.sleep(1)

    def serve_order(self):
        time.sleep(2)
        while True:    
            if self.lisst !=0:
                print(f'serving order: {dharm.lisst.pop()}')
                time.sleep(4)  
                print({time.ctime()})
            if len(self.lisst) == 0:
                print(' your order is completed')
                break
            
dharm = Queue()
dharm.place_order('pizza,fries,nutella')  
dharm.serve_order()

print(f'execution stop: {time.ctime()}')