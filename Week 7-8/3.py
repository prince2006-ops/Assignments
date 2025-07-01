import numpy as np
user_input=[]
print("Enter 10 numbers")
while len(user_input)<10:
    num=int(input(f"Enter the number {len(user_input)+1} :"))
    user_input.append(num)

arr=np.array(user_input)
sort_value=np.sort(arr)
reshaped_matrix_1=sort_value.reshape(2,5)
reshaped_matrix_2=sort_value.reshape(5,2)
print("The sorted value is",sort_value)
print("The first reshaped matrix is:")
print(reshaped_matrix_1)
print("The second reshaped matrix is:")
print(reshaped_matrix_2)