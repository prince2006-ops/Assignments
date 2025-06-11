#separate functions for different calculation
def add(first_value,second_value):  #for addition
    add_value=first_value+second_value
    return add_value
def sub(first_value,second_value): #for subtraction
    sub_value=first_value-second_value
    return sub_value
def mul(first_value,second_value):#for multiplication
    mul_value=first_value*second_value
    return mul_value
def div(first_value,second_value): #for division
    div_value=first_value/second_value
    return div_value
def mod(first_value,second_value): # for multiplication
    mod_value=first_value % second_value
    return mod_value
def floor(first_value,second_value):# for floor division
    floor_value=first_value // second_value
    return floor_value


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(f"The sum is {add(a,b)}")
print(f"The difference is {sub(a,b)}")
print(f"The product is {mul(a,b)}")
print(f"The division is {div(a,b)}")
print(f"The modulus is {mod(a,b)}")
print(f"The floor division is {floor(a,b)}")



