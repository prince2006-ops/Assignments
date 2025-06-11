book_details={}
while True:
    book_title=input("Enter the book name:")
    book_author=input("Enter the book author's name:")
    isbn_number=int(input("Enter the ISBN number:"))
    cost=(input("Enter the price of book:"))
    book_details[isbn_number] = {
        'title':book_title,
        "author":book_author,
        "price":cost
    }
    choice=input("Do you want to continue(y/n)?").strip().lower()
    if choice=="n":
        break
print(" Book details")
for key,value in book_details.items():
        print(f"\nISBN: {isbn_number}")
        print(f"Title: {value['title']}")
        print(f"Author: {value['author']}")
        print(f"Price: ${value['price']}")

