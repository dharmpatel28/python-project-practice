# module: python files contains functions and classes wrote by developers.

# debugging: the process of identifying and removing errors from computer hardware or software.

# why debugging
# 1. our program is not running and causing unexpected error
# 2. our program is working but not in the way we want

import pdb  # module

pdb.set_trace() # it can be used anywhere in the code, where you thinnk possibility of error 
#  set trace will give error after executing every statement line by line

#BEFORE
# name = input("enter name: ")
# age = input("Enter age: ")
# print(f"hello {name} your age is {age}")
# age2 = age + 5 # this line consist of error 
# print(f"hello {name} you will {age2} in next five years")

# AFTER executing of set_trace method
name = input("enter name: ")
age = int(input("Enter age: "))
print(f"hello {name} your age is {age}")
age2 = age + 5 # this line consist of error 
print(f"hello {name} you will {age2} in next five years")

#l : this command shows which statement is going to be executed
#n : this command used to execute the statement
#q : is uses to stop the execution of set_trace method
#c: it used after the process of set_trace(), to run the program 