#solving various expressions
a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))
c=int(input("Enter a number c:"))
#I.	a2 + 2ab + b2
first_expression= (a**2+2*a*b+b**2)
print(f"The value of first expression is:{first_expression} ")
# II.	a5 + 2abc + b3 + c4
second_expression= (a**5+2*a*b*c+b**3+c**4)
print(f"The value of second expression is:{second_expression} ")
#III.	a7 + 5a3b2c6 + b7
third_expression=(a**7+5*(a**3)*(b**2)*(c**6)+b**7)
print(f"The value of third expression is:{third_expression} ")


