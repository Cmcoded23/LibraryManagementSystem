# Defined a variable to store the data
books = [
    {
        "Title": "Sorcerer's Ring",
        "Author": "Morgan Rice",
        "isb No.": "3456",
        "Availability": "True"
    },
]


# Defined a class
class Book:

    def __init__(self, title, author, isbn, availability="True"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        books.append({
            "Title": self.title,
            "Author": self.author,
            "isb No.": self.isbn,
            "Availability": self.availability
        })

# Now a class Library to manipulate our stored data


class Library:
    # A method that allows us to borrow books, and doesnt allow to borrow whats been borrowed
    def borrow_book(search_name):
        for book in books:
            if search_name.lower() == book["Title"].lower():
                if book["Availability"] == "True":
                    print("Book Found")
                    book["Availability"] = "False"
                    print("Book Borrowed")
                elif book.get("Availability") == "False":
                    print("Book Already Borrowed")
# A method allowing us to return books

    def return_book(search_name):
        for book in books:
            if search_name.lower() == book["Title"].lower():
                if book["Availability"] == "False":
                    print("Book Returned")
                    book.get("Availability") == "True"
                elif book["Availability"] == "True":
                    print("Book In Library, Already Returned")
# A method allowing us to check if a book is available

    def search_book(search_input):
        for book in books:
            if search_input.lower() == book["Title"].lower():
                print('Book Found')
                break
        if search_input not in [book.get("Title")]:
            print("Not Found")


class Ebook(Book):
    def __init__(self, title, author, isbn, file_size, format, availability=True, type="Ebook"):
        super().__init__(title, author, isbn, availability)
        self.size = file_size,
        self.format = format,
        self.__type = type
        books.append(
            {
                "Title": self.title,
                "Author": self.author,
                "Isb No.": self.isbn,
                "Availability": self.availability,
                "File Size": self.size,
                "File Format": self.__type,

            }
        )


book_2 = Book("MY Favorite Son", "Wizzy", "3455")
book_3 = Book("MY Favorite boy", "steezy", "3255")
book4 = Book("MY Favorite girl", "swinzzy", "12455")

Library.borrow_book("My favorite Son")
Library.return_book("mY Favorite Son")
