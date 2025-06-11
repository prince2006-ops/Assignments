#percentage and division calculations of the students
print("Enter the marks for the five subjects:")
#taking input in form of list
marks=[]
for i in range(5):
    mark=float(input())
    marks.append(mark)
#performing calculations
Total=sum(marks)
print(f"Your total is {Total}")
average=Total/5
print(f"Your average is {average}")
percentage=(Total/500)*100
print(f"Your percentage is {percentage}%")
if percentage>=80:
    print("Congratulations! You got distinction")
elif percentage>60:
    print("Congratulations! You got first division")
elif percentage>50:
    print("Congratulations! You got second division")
elif percentage>45:
    print("Congratulations! You got third division")
else:
    print("Sorry! You are failed")

