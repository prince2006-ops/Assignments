#sorting the names in list
names=[]
def name_list(name):
    names.append(name)
    names.sort()


while True:
    name = input("Enter the name or 'exit' to quit: ").strip().capitalize()
    if name == "Exit":
        break
    name_list(name)
print(names)
