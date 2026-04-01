import csv
import json
import io

# Step 1: Interactive input
students = []
num = int(input())  # <-- remove prompt text for online compilers

for i in range(num):
    name = input()  # Student name
    math = int(input())  # Math marks
    science = int(input())  # Science marks
    english = int(input())  # English marks
    
    total = math + science + english
    average = round(total / 3, 2)
    
    student = {
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Average": average
    }
    students.append(student)

# Sort students by average
students_sorted = sorted(students, key=lambda x: x['Average'], reverse=True)

# Display results
for student in students_sorted:
    print(f"{student['Name']} - Total: {student['Total']}, Average: {student['Average']}")

top_student = students_sorted[0]
print(f"Top Student: {top_student['Name']} with Average: {top_student['Average']}")

# Generate CSV and JSON in memory
csv_output = io.StringIO()
writer = csv.DictWriter(csv_output, fieldnames=["Name","Math","Science","English","Total","Average"])
writer.writeheader()
writer.writerows(students)
print("\nCSV Data:")
print(csv_output.getvalue())

json_content = json.dumps(students, indent=4)
print("\nJSON Data:")
print(json_content)
