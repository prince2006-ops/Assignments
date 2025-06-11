     #serching the index of the city
def cities_index(cities_list,user_input):
    if user_input in cities_list:
        return cities_list.index(user_input)
    else:
        return "Cities is not in list"
cities_names=['Sydney','Melbourne','Perth','Adelaide','Brisbane','Canberra','Hobart','Darwin']
while True:
    user_city=input("Enter the city:").capitalize().strip()
    result=cities_index(cities_names,user_city)
    print(result)
