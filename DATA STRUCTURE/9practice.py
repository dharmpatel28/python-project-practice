def bubblesort(data,key=' '):

    size = len(data) -1

    for j in range(size):
        
        for i in range(size):
            
            if data[i][key] > data[i+1][key]:   #data[i][key] gives value of particular key
            # if key in dictionaries:
                # return data[i][key] # [0] for list and [key] because dictionary

                # used to swap key,value pairs inside dictionaries
                # temp = data[i][key]
                # data[i][key] = data[i+1][key]
                # data[i+1][key] = temp

                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                
    return data
            

dharm = bubblesort([{ 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
                   { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
                   { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
                   { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}], 
                   key='transaction_amount')

for answer in dharm:
    print(answer)    