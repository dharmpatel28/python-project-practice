# writer and DictWriter

from csv import writer
with open('225file1.csv','w', newline='') as f: # this newlinw will avoid empty lines in csv file
    csv_write = writer(f)

    # to write in csv file there are two methods: writerow and writerows
    # csv_write.writerow(['name', 'country'])
    # csv_write.writerow(['dharm', 'india'])
    # csv_write.writerow(['dhruv', 'india'])

    csv_write.writerows([['name', 'country'], ['dharm', 'india'], ['dhruv', 'india']]) #2list