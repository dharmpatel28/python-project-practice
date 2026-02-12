import time

start=time.time()
def linear_search(data, targetvalue):
    
    iteration = 0
    for index,element in enumerate(data):
        iteration += 1
        if element  == targetvalue:    
            print(f'index is: {index}')
            print(f'no. of iteration is: {iteration}')

# linear_search(range(1,100000),99999)
linear_search([1,3,4,4,5,6],4)

stop=time.time()
print(f'{(stop-start)*1000} miliseconds')