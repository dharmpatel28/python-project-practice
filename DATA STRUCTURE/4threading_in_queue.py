# for stack self.container is obejct and for queue self.buffer is object
from collections import deque
import time
import threading

# queue = deque()
# queue.append('1')
# queue.appendleft('2')
# print(queue)

# another method
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,value):
        return self.buffer.appendleft(value)
    
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def length(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0 
     
foodorder=Queue()
print(f'5. execution start: {time.ctime()}')
def place_order(self,orders):
    for element in orders.split(','):
        print(f'placing order for: {element}')
        foodorder.enqueue(element)
    time.sleep(2)

def serve_order():
    time.sleep(1)
    while True:
        order = foodorder.dequeue()
        print(f'Now serving: {order}')
        time.sleep(4)

if __name__ == '__main__':
    orders = ['pizza']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)  
    t1.start()
    t2.start()         

        
# dharm = Queue()
# # dharm.enqueue('one')
# # dharm.enqueue('two')
# # print(f'2. {dharm.length()}')
# # print(f'3.{dharm.is_empty()}')
# dharm.place_order('pizza')
# print(f'1.{dharm.buffer}')
# print(f'5. execution stop: {time.ctime()}')


