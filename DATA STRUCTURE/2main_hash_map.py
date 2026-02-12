class Hashtable():
    def __init__(self):
        self.max = 50
        self.lisst = [None for i in range(self.max)]

# generate location or ascii value for key
    def ascii(self,key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.max

    
    def __setitem__(self,key,value):
        excel={}
        h = self.ascii(key)
        self.lisst[h] = value
        excel[key] = value
        # print(excel)

    def __getitem__(self,key):
        h = self.ascii(key)
        return f'the value of {key} is {(self.lisst[h])}\n'

    def __delitem__(self,key):
        h = self.ascii(key)
        self.lisst[h] =  'deleted' 
        # print(self.lisst[h])       

dharm = Hashtable()
dharm['march 1'] =11 # because __setitem__
dharm['march 2'] = 12
dharm['march 3'] = 13
dharm['march 20'] = 14
dharm['may 28'] = 'birthday'

print(dharm['march 2'])

del dharm['march 3']

print(dharm.lisst)

# dharm.delete('march 3')
# dharm.add('march 1','11')
