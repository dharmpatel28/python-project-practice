# create your generator with generator function
# generator first print the result and then remove the result from memory

# 1. generator function

def nums(n):
    for i in range(1,n+1):
        yield(i)

number = list(nums(10))

for num in number:
    print(num)
   

# for num in number:
#     print(num)  it does not print second time because generator function will remove after it print the result   