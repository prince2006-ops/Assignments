#Factorial of a given number
input_value=input("Enter a number:")
fact=1
if input_value.isdigit():
    number=int(input_value)
    for i in range(1, number+1):
        fact *=i
    print(f"The factorial is {fact}")

