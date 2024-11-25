# import csv
#
# with open("employees.csv", 'a') as out_file:
#     writer = csv.writer(out_file)
#     writer.writerow(["Jenny Scoot", 2500])

import csv

with open("employees.csv") as in_file:
    reader = csv.reader(in_file)
    for row in reader:
        print(row)