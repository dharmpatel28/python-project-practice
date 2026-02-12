from csv import DictWriter
with open('226file1.csv','w', newline='') as f:
    csv_write = DictWriter(f, fieldnames =['name','country','age'])
    csv_write.writeheader() # to write header

    # csv_writer.writerow({
    #     'name': 'dharm',
    #     'country': 'india',
    #     'age': 21
    # })

    # csv_writer.writerow({
    #     'name': 'dhruv',
    #     'country': 'india',
    #     'age': 21
    # })

    # csv_write.writerows([dict,dict,dict])

    csv_write.writerows([
        {'name': 'dharm', 'country': 'india', 'age': 21},
        {'name': 'dharm', 'country': 'india', 'age': 21},
        {'name': 'dharm', 'country': 'india', 'age': 21}
    ])