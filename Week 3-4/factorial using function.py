# factorial using functions

def factorial(fact):
    if fact<0:
        return "not possible"
    elif (fact==0) or (fact==1):
        return 1
    else:
        factorial_value=1
        for i in range(1,fact+1):
            factorial_value *=i
        return factorial_value

user_input=int(input("Enter any non-negative number to calculate factorial:"))
print(f"The factorial value is {factorial(user_input)}")