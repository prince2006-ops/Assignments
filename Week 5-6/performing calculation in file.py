from  datetime import datetime
while True:
    with open('calculation.txt','a')as file:
        now = datetime.now()
        num_1=int(input("Enter the 1st number:"))
        num_2=int(input("Enter the 2nd number:"))
        file.write(f"Date and Time:2{now}\n")
        file.write(f"Number_1={num_1}\n")
        file.write(f"Number_2={num_2}\n")
        sum=num_1+num_2
        difference=num_1-num_2
        multiplication=num_1*num_2
        division=num_1/num_2
        file.write(f"Sum={sum}\n")
        file.write(f"Difference={difference}\n")
        file.write(f"Product={multiplication}\n")
        file.write(f"Division={division}\n")
        file.write("*******************************")
        file.close()

    with open('calculation.txt','r')as file:
        read=file.read()
        print(read)
        file.close()
    choice=input("Do you want to continue(y/n)?")
    if choice=='n':
        break
