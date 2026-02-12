# if you want to save 2 tuple at one location than collision handling is used
    
class Hashtable:
    def __init__(self):
        self.max = 20
        self.lisst = [[] for i in range(self.max)]

    def ascii(self,key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.max

    def __setitem__(self,key,value):
        h = self.ascii(key)
        found =False
        for index,elements in enumerate(self.lisst[h]): # to update the value for same key
            if len(elements) == 2 and elements[0] == key:
                self.lisst[h] = (key,value)
                found = True
                break
        
        if not found: #to add key-value pair which has same ascii value  
            self.lisst[h].append((key,value))

    def __getitem__(self, key):
        h = self.ascii(key)
        for element in self.lisst[h]:
            if element[0] == key:
                return f'the value of {key} is  {element[1]}'

    def __delitem__(self, key):
        h = self.ascii(key)
        for element in self.lisst[h]:
            del self.lisst[h]


    
dharm = Hashtable()
dharm['march 7'] = 120
dharm['march 7'] = 2
dharm['march 17'] = 459

print(dharm['march 17'])

del dharm['march 17']

print(dharm.lisst)
