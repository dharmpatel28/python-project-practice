numbers = [1,2,3,4] # list, string,tuple are iterable
squares = map(lambda i : i**2, numbers) # iterator
# for i in numbers:
#     print(i)

# how for loop works
# step 1: step call iter function
# step 2: iter(numbers) ----> now this is iterator
# step 3: next(iter(numbers)).. this will print the number like 1,2,3,4    

# now 
numbers = [1,2,3,4] 
number_iter = iter(numbers)
print(next(number_iter)) # print 1
print(next(number_iter)) # print 2........

print(" ")

squares = map(lambda i : i**2, numbers) # this is iterator so we can directly move to step 3
print(next(squares)) #print square of 1
print(next(squares)) #print square of 2....