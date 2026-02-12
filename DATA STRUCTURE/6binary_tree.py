class Binarytree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data: # already availabel
            return

        if data < self.data:
            if self.left: # if already availabel in left
                self.left.add_child(data)
            else:
                self.left = Binarytree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binarytree(data)

    def in_order_traversal(self):
        elements =[]
        if self.left: # visit left tree
            elements = elements + self.left.in_order_traversal()

        elements.append(self.data) # base node
        
        if self.right: # visit right tree
            elements = elements + self.right.in_order_traversal()

        return elements
    
    def preorder_traversal(self):
        elements1=[]
        elements1.append(self.data) # base node

        if self.left: # visit left tree
            elements1 = elements1 + self.left.preorder_traversal()

        if self.right: # visit right tree
            elements1 = elements1 + self.right.preorder_traversal()

        return elements1  

    def postorder_traversal(self):
        elements2=[]
       
        if self.left: # visit left tree
            elements2 = elements2 + self.left.postorder_traversal()

        if self.right: # visit right tree
            elements2 = elements2 + self.right.postorder_traversal()

        elements2.append(self.data) # base node
    

        return elements2      

    def search(self,value):
        if value == self.data:
            print('exist')

        if value < self.data:
            if self.left:
                self.left.search(value)
            else:
                print('values does not exist')

        if value > self.data:
            if self.right:
                self.right.search(value)
            else:
                print('values does not exist')

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self,value): # approach 1
        if value < self.data:
            if self.left:
                self.left =(self.left.delete(value))
        elif value > self.data:
            if self.right:
                self.right = (self.right.delete(value))    
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_value =  self.right.find_min()
            self.data = min_value 
            self.right=self.right.delete(min_value)     

        return self    

dharm = Binarytree(15)
dharm.add_child(12)
dharm.add_child(27)
dharm.add_child(7)
dharm.add_child(14)
dharm.add_child(20)
dharm.add_child(88)
dharm.add_child(23)

dharm.delete(27)
print(f'in_order traversal list: {dharm.in_order_traversal()}')
print(f'preorder traversal list: {dharm.preorder_traversal()}')
print(f'postorder traversal list:  {dharm.postorder_traversal()}')
dharm.search(100)
print(dharm.find_min())

    