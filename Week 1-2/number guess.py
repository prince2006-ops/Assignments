# number guessing game in python
import random
print("Enter the number between 1 to 10")
print("You have 5 chances")
answer=random.randint(1,10)
for i in range(1,6):
    user_input=int(input(f"Enter the number attempt {i}:"))
    if user_input>10:
        print("Out of range!!")
    elif user_input<answer:
        print("The number is low")
    elif user_input>answer:
        print("The number is high")
    else:
        print("Congratulation!🎉🎉 Correct answer")
        break
print(f"The number was {answer}")