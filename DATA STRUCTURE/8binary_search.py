# this is faster than linear search

# import time

# start=time.time()

def binary_search(data,targetvalue):
    
    leftindex=0
    rightindex=len(data)-1
    midindex=0

    while leftindex <= rightindex:
        midindex=(leftindex+rightindex)//2
        midvalue=data[midindex]
        # print(midvalue)

        if midvalue == targetvalue:
            return (midindex)
        
        elif  targetvalue < midvalue:
            rightindex = midindex - 1

        else:
            leftindex = midindex + 1
        
    return "value doesn't exist"


# dharm =binary_search(range(1,100000),99999)
# print(f'index of target value is : {dharm}')

# dharm =binary_search([11,15,15,15,17,21],15)
# print(f'index of target value is : {dharm}')

# stop=time.time()
# print(f'{(stop-start)*1000} miliseconds')


def multi_index(data, targetvalue):
    
    index = binary_search(data,targetvalue)

    indices = [index]
    
    # if in left side
    i = index - 1
    while i >=0 :
        if data[i] == targetvalue:
            indices.append(i)
        else: 
            break                      # what to do if no match
        i = i - 1    

    # if in right side
    i = index + 1
    while i < len(data):
        if data[i] == targetvalue:
            indices.append(i) 
        else:
            break
        i = i + 1      

    return sorted(indices)

dharm1 = multi_index([11,12,15,15,15,15,17,21],17)
print(dharm1)
