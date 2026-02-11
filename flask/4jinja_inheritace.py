# # you ca inheritance one file to another like you have to inherit same layout in every file

# step 1: in layout file add your layout code which is going to be same in every file
# step 2 : {% block body %} {% endblock %} add this code in layout file,
#         this code indicates main file code and this code in place of main code in layout file

# step3 : in main file add '{% extends "layout.html" %}' above the whole code in main file
#         below this code write '{% block body %}' this code 
#         then write main code in file
#         then add '{% endblock %}' at the end of code 