import csv

with open("example.csv", mode='w', newline='') as file:
    writer= csv.writer(file)
    writer.writerow(["Name" , "Age" , "Phone" , "Fname"])
    writer.writerow(["Alex", "18", "0000000000", "Sample Parent"])

with open("example.csv", mode='r') as file:
    reader=csv.reader(file)
    for read in reader:
        print (read)