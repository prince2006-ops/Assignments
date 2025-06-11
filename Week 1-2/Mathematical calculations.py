        #advance mathematical calculations
import math
user_input=float(input("Enter the number:"))
#1.square of the number
square=math.pow(user_input,2)
print(f"The square is {square}")
#2.square root of a number
if user_input>=0:
    square_root=math.sqrt(user_input)
    print(f"The square root is {square_root} ")
else:
     print("The square root of the number is not possible")
#3.exponential value of the number
exponential=math.exp(user_input)
print(f"The exponential value is {exponential}")
#4. log base 10
if user_input>0:
    log=math.log10(user_input)
    print(f"The log 10 is {log}")
else:
    print("The log 10 of this number is not possible")
#5. Power of 3,4,5
pow_3=pow(user_input,3)
print(f"The power of 3 is {pow_3}")
pow_4=pow(user_input,4)
print(f"The power of 4 is {pow_4}")
pow_5=pow(user_input,5)
print(f"The power of 5 is {pow_5}")


