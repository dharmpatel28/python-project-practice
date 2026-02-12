# read and write together
from csv import DictWriter, DictReader

with open('227file1.csv','r') as rf:
    with open('227file2.csv','w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames = ['name1', 'country1', 'age1'])
        csv_writer.writeheader()

        for row in csv_reader:
            print(row['name'], row['country'], row['age'])

            csv_writer.writerows([{
                'name1': row['name'],'country1': row['country'],'age1': row['age']
            }])    
