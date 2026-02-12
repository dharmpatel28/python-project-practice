# "self.head" simply refers to where you are whilst traversing the list, 
# so what is the difference between saying: "Self.head is the current node, 
# so self.head.next is the next node"

# A single node of a singly linked list
class Node:
  # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self, head=None):
        self.head = None

    # insertion method for the linked list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node # pointer for next node

    # print method for the linked list
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        list1 = []
        while itr:
            list1.append(itr.data)
            itr = itr.next
        print(list1)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next: # pointer is not at last node
            itr=itr.next
        itr.next = Node(data,None) 

    def insert_values(self, values):
        self.head = None
        for data in values:
            self.insert_at_end(data)

    def length(self):
        count=0
        itr =self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.length():
            return 'invalid index'

        if index == 0:
            self.head = self.head.next # current node = next node
            return

        count = 0
        itr = self.head # current node
        while itr:
            if count == index - 1: 
                itr.next = itr.next.next # itr.next is element that we have to remove and itr.next.next is element which comes next to it
                break            
            itr = itr.next
            count +=1

    def insert_at(self, index,data):
        if index < 0 or index >= self.length():
            return 'invalid index'      

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index- 1:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next 
            count = count + 1 

#---------------------- do it by my own----------------------------------------#
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
#-------------------------------------------------------------------------------------------

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert_at_beginning(3)
LL.insert_at_beginning(4)
LL.insert_at_beginning(5)
LL.insert_at_end(100)
LL.insert_at_end(['dharm', 'patel'])

LL.remove_at(2)
LL.insert_at(2,'two')
LL.insert_after_value(['dharm', 'patel'],'three')
LL.remove_by_value(['dharm', 'patel'])
print(LL.length())
LL.print()
