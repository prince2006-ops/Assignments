import numpy as np
user_input=[]
choice=int(input("Enter the number of input you want? Should be greater than 10:"))
while choice<10:
    choice=int(input("Enter the number of input you want? Should be greater than 10:"))
while len(user_input)<choice:
    num=int(input("Enter the number"))
    user_input.append(num)

arr=np.array(user_input)
sort_value=np.sort(arr)
print("The sorted value is",sort_value)
num_2_5= sort_value[2:5]
num_5_8=sort_value[5:8]
num_2_9=sort_value[2:9]
print("The sorted value from 2 to 5 is:",num_2_5)
print("The sorted value from 5 to 8 is:",num_5_8)
print("The sorted value from 2 to 9 is:",num_2_9)
