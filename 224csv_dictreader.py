# from csv import DictReader

# with open('224file1.csv', 'r') as f:
#     csv_reader = DictReader(f)

#     for row in csv_reader:
#         print(row) # also you can print print(row['email] for every emails
        
# if data is separated by other sign such as "|" instead of "," then below method is used

from csv import DictReader

with open('224file1.csv', 'r') as f:
    csv_reader = DictReader(f,delimiter='|') # change is only in this line

    for row in csv_reader:
        print(row)   