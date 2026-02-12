# numbers = list(range(1,11)) # generate list using range function
# print(numbers)

# print(f"poped value : {numbers.pop()}") # it also print the pop value and also store in some variable
# print(numbers)

# list = [1,2,4,5,6,7,8,9,10,11,12,13,1,14,15,16]
# print(list.index(1 , 10 , 15 ))   # 1 = number wants to find , 10 = stating position of search , 15 = ending pos

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

prin = list(range(1,11))
print(negative_list(prin))        