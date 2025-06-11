#Even and Odd in separate list
Even=[]
Odd=[]
size=int(input("How many numbers do you want to input:")) # asking user to tell number of loops
for i in range (size):
    user_input=input("Enter a number:")
    if user_input.isdigit():
        number=int(user_input)
    else:
        quit()
    if number%2==0:               # checking even odd
        Even.append(number)
    else:
        Odd.append(number)
print(f"The even number list is {Even}")            #printing out the list
print(f"The odd number list is {Odd}")