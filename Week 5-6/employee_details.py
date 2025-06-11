import  csv
class employee():
    def __init__(self,emp_id,name,address,contact,spouse,child_number,salary):
        self.id=emp_id
        self.name=name
        self.address=address
        self.contact=contact
        self.spouse=spouse
        self.child_no=child_number
        self.salary=salary

    def Display(self):
        return [
            self.id,
            self.name,
            self.address,
            self.contact,
            self.spouse,
            self.child_no,
            self.salary
        ]
def add_employees():
    try:
        with open("employees.csv", "a") as file:
            file.write("EmpID,Name,Address,Contact,Spouse,Children,Salary\n")
            while True:
                empid = input("Employee ID: ")
                name = input("Name: ")
                address = input("Address: ")
                contact = input("Contact Number: ")
                spouse = input("Spouse Name: ")
                children = input("Number of Children: ")
                salary = input("Salary: ")

                emp = employee(empid, name, address, contact, spouse, children, salary)
                line = f"{empid},{name},{address},{contact},{spouse},{children},{salary}\n"
                file.write(line)
                more = input("Add another employee? (yes/no): ").lower()
                if more != "yes":
                    break
    except Exception as e:
        print("Error:", e)

def show_employees():
    try:
        with open("employees.csv", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No employee data found.")

add_employees()
show_employees()


