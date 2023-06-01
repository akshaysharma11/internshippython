import csv

filename="tests_state_wise.csv"
rows=[]
cols=[]

with open(filename,"r") as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
print(rows)