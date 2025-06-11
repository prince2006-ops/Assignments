#separating even and odd and calculating the sum

even=[]
odd=[]
while True:
    user_input=input("Enter the number or exit to end:").strip().lower()
    if user_input=="exit":
        break
    if user_input.isdigit():
        number=int(user_input)
        if number%2==0:                   #checking even or odd
            even.append(number)
        else:
            odd.append(number)

print(f"The sum of even digit is :{sum(even)}")
print(f"The sum of odd digit is :{sum(odd)}")



