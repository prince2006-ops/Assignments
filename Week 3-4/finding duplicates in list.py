#removing the duplicates from list
def list_items(user_list):
    items=user_list.split(',')      #splitting the value in list after comma
    non_duplicates=list(set(items))     # converting list to set
    return sorted(non_duplicates)       #sorting the value
user_lists=input("Enter the value in list using comma")
print(list_items(user_lists))

