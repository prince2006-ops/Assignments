def Occurance(numbers):
    repeated={}
    #loop for finding the occurance
    for num in numbers:
        if num in repeated:
            repeated[num]+=1
        else:
            repeated[num]=1
    #loop for displaying dictionary
    for key,value in repeated.items():
        print(f"{key}:{value}")

print("First case:")
Occurance([1,2,3,2,3,4,5,6,4,5])
print("Second case:")
Occurance([1,8,3,2,3,7,5,6,8,5])