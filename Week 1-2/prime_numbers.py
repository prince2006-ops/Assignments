# prime numbers between 2 digits:

start_value=int(input("Enter the number:"))
last_value=int(input("Enter the number:"))
total=0
for number in range(start_value,last_value+1):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)
            total=total+number
print(f"The total is {total}")




