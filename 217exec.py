with open("217file1.txt", "r") as rf:
    with open("217file2.txt", "a") as af:
        for line in rf.readlines():
            name,salary = line.split(",")
            af.write(f"{name}\'s salary is {salary}")