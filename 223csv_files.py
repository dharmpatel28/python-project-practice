from csv import reader

with open('223file1.csv','r') as f:
    csv_reader = reader(f)
    print(csv_reader)

    next(csv_reader) # it will not print the first line
    for row in csv_reader:
        print(row)