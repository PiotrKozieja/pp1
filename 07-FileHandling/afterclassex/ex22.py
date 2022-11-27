import csv
nl = 0
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        if nl >0:
            if int(line[2]) < 30:
                print(f"{line[0]} {line[1]} {line[4]}")
        nl = nl+1