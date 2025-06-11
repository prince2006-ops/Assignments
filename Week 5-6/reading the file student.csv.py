import csv
with open('student.csv','r') as file:
    read = csv.DictReader(file)
    for row in read:
        print(f"Name:{row['name']}")
        print(f"Id:{row['id']}")
        print(f"Course:{row['course']}")
        print(f"Level:{row['level']}")
        print(f"Section:{row['section']}")
        print("*************************")