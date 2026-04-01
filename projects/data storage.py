import csv
import io

file = io.StringIO()
writer = csv.writer(file)

writer.writerow(["ID", "Name", "Salary", "Department"])


n = int(input())


for i in range(n):
    emp_id = input()
    name = input()
    salary = input()
    dept = input()
    
    writer.writerow([emp_id, name, salary, dept])

file.seek(0)

reader = csv.reader(file)

for row in reader:
    print(" | ".join(row))
