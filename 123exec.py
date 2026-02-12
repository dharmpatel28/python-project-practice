user = {}

name = input("enter name: ")
age = input("enter age: ")
fav_movies = input("enter fav_movies: ").split(" , ")
fav_song = input("enter fav_song:").split(" , ")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_song

# print(user)
for key, value in user.items():
    print(f"{key} : {value}")


#     $ python 123exec.py 
# enter name: dharm
# enter age: 21
# enter fav_movies: e,d
# enter fav_song:w
# name : dharm
# age : 21
# fav_movies : ['e,d']
# fav_song : ['w']