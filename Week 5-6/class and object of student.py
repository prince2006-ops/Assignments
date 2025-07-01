class Student:
    def __init__(self,id,name,address,admission_year,level,section):
       self.id=id
       self.name=name
       self.address=address
       self.admission=admission_year
       self.level=level
       self.section=section

    def display(self):
        print("\n********** Student Details ***********")
        print(f"ID:{self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

id=input("Enter the ID: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = int(input("Enter Level: "))
section = input("Enter Section: ")
student_detail=Student(id, name, address, admission_year, level, section)

student_detail.display()