import csv            #imporating cvs library
number_of_input=int(input("Enter the number of input:"))
with open('student.csv','w',newline='')as file:
    write=csv.writer(file)
    write.writerow(['name','id','course','level','section'])   # header of the file

    for i in range(number_of_input):
        print(f"Enter the detail of student{i+1}")
        name=input("Name: ")                                          #writing in the file
        id=int(input("Id:"))
        course=input("Course:")
        level=input("Level:")
        section=input("section:")
        write.writerow([name, id, course, level, section])

with open('student.csv','r')as file:
    read=csv.DictReader(file)    # reading as a directory from a file
    for row in read:
        print(f"Name:{row['name']}")
        print(f"Id:{row['id']}")
        print(f"Course:{row['course']}")
        print(f"Level:{row['level']}")
        print(f"Section:{row['section']}")
        print("*************************")
