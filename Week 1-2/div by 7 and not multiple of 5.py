#Numbers that are divisible by 7 but are not a multiple of 5 between 2000 and 3200


# print("Numbers that are divisible by 7 but are not a multiple of 5 between 2000 and 3200 are:")
# for number in range(2000,3201):
#     if (number%7==0) and (number%5!=0):
#         print(number)


start_value=int(input("Enter the number:"))
last_value=int(input("Enter the number:"))
print("Numbers that are divisible by 7 but are not a multiple of 5 are:")
for number in range(start_value,last_value+1):
    if (number%7==0) and (number%5!=0):
        print(number)
