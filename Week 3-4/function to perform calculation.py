#function to perform mathematical calculations
def calculation():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    add=a+b
    print(f"The sum is {add}")
    sub=a-b
    print(f"The difference is {sub}")
    mul=a*b
    print(f"The product is {mul}")
    mod=a%b
    print(f"The modulus is {mod}")

calculation()
