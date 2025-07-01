import os

class Book:
    def __init__(self, title, author):
        self.title = title.strip()
        self.author = author.strip()

class Library:
    def __init__(self, file="books.txt"):
        self.file = file
        self.books = []
        self._load()

    def _load(self):
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                f.write("Atomic Habit,George Orwell\nThe Notebook,J.R.R. Tolkien\n")
        with open(self.file, "r") as f:
            for line in f:
                if line.strip():
                    title, author = line.strip().split(",", 1)
                    self.books.append(Book(title, author))

    def _save(self):
        with open(self.file, "w") as f:
            for b in self.books:
                f.write(f"{b.title},{b.author}\n")

    def search(self, keyword):
        found = False
        for b in self.books:
            if keyword.lower() in b.title.lower():
                print(f"{b.title} by {b.author}")
                found = True
        if not found:
            print("Book not found.")

    def issue(self, title):
        for i, b in enumerate(self.books):
            if b.title.lower() == title.lower():
                self.books.pop(i)
                self._save()
                print("Book issued.")
                return
        print("Book not available.")

    def return_book(self, title, author):
        self.books.append(Book(title, author))
        self._save()
        print("Book returned/added.")

def main():
    lib = Library()
    while True:
        print("\n1. Search  2. Issue  3. Return  4. Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1":
                lib.search(input("Search title: "))
            elif choice == "2":
                lib.issue(input("Enter title to issue: "))
            elif choice == "3":
                t = input("Enter title to return: ")
                a = input("Enter author name: ")
                lib.return_book(t, a)
            elif choice == "4":
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
