def bubblesort(data):
    
    size = len(data) -1 
    for j in range(size):
        # print(f'j is {j}')

        for i in range(size):
            # print(f' i is {i}')
            # print(data)
            
            if data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
    return data
        
    
    
        

dharm = bubblesort([3,1,4,0,9,2,1000,763,999,23])
print(dharm)