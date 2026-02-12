class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('List is Empty..')
        
        itr = self.head 
        list2=[]
        while itr:
            list2.append(itr.data)
            itr = itr.next
        print(list2)

    def insert_at_end(self, data):
        if self.head is None:
            self.head =Node(data,None)
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.length():
            raise Exception("invalid index value")

        if index == 0:
            self.head = self.head.next
            return

        count = 0 
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
            itr = itr.next
            count = count + 1  

    def insert_at(self,index,data):
        if index<0 or index>=self.length():
            raise Exception("invalid index value")
        
        if index == 0: 
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node 
            itr = itr.next 
            count = count + 1    

    def insert_after_value(self, dataafter,datainsert):
       
        itr = self.head
        while itr:
            if itr.data == dataafter:
                node = Node(datainsert,itr.next)
                itr.next = node
            itr = itr.next
           

    def remove_by_value(self,data):
      
        itr = self.head
        while itr:
            if itr.data == data:
                itr.data= itr.next.data
                itr.next = itr.next.next
            itr = itr.next        
        
dharm= LinkedList()

dharm.insert_at_beginning('beginning')
dharm.insert_at_beginning(1)
dharm.insert_at_beginning(2)
dharm.insert_at_end('end')
dharm.remove_at(1)
# dharm.remove_at(5) # gives error
dharm.insert_at(1,'one')
dharm.insert_after_value('one','three')
dharm.remove_by_value(2)
print(f'length of LinkedList is : {dharm.length()}')

dharm.print()