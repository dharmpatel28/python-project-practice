fruits1 = ["mango", "grapes"]
fruits1.insert(1, "orange")          # to add fruit at specific position
print(f" 1.{fruits1}")

fruits2 = ["banana", "plum"]

fruits = fruits1 + fruits2           # to concatenate two list
print(f" 2.{fruits}")

# fruits1.extend(fruits2)              # fruits of fruits2 add in fruits1
# print(f" 3.{fruits1}")
# print(f" 4.{fruits2}")

fruits1.append(fruits2)              # whole list of fruits2 add in fruits1
print(f" 5.{fruits1}")


#output: 
# Dharm Patel@DHARM MINGW64 /f/py tutorial
# $ python 84add_data_methods.py
#  1.['mango', 'orange', 'grapes']
#  2.['mango', 'orange', 'grapes', 'banana', 'plum']
#  3.['mango', 'orange', 'grapes', 'banana', 'plum']
#  4.['banana', 'plum']
#  5.['mango', 'orange', 'grapes', ['banana', 'plum']]