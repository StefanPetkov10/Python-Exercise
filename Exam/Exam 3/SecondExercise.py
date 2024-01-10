class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def print_information(self):
        return print(f"{self.book_name}, {self.book_code}, {self.book_price}, {self.book_year}, {self.book_author}")

book1 = Book("Python", 1, 10, 2010, "Someone")
book1.print_information()

books = []
# for _ in range(4):
#     book_name = input("book_name - ")
#     book_code = int(input("book_code"))
#     book_price = int(input("book_price"))
#     book_year = int(input("book_year"))
#     book_author = input("book_author")
#     books.append(Book(book_name, book_code, book_price, book_year, book_author))

books.append(Book("Python", 1, 10, 2010, "Someone"))
books.append(Book("C#", 2, 10, 2010, "Someone"))
books.append(Book("C#", 2, 10, 2010, "Someone"))
def sort_by_name():
    sorted_book = sorted(books, key=lambda book: book.book_name, reverse= True)
    for book in books:
        print(book.book_name)

sort_by_name()

def group_books_by_author(book_list):
    author_dict = {}
    for book in book_list:
        author = book.book_author
        if author in author_dict:
            author_dict[author].append(book)
        else:
            author_dict[author] = [book]
    return author_dict

books_by_author = group_books_by_author(books)

for author, author_books in books_by_author.items():
    print(f"Books by {author}:")
    for book in author_books:
        print(f"- {book.book_name}")
    print()

def search_by_code(book_code):
    books_by_code = [code for code in books if code.book_code == book_code]
    return books_by_code



books_by_code = search_by_code(2)
if len(books_by_code) < 1:
    print("The book is not found")
else:
    for year in books_by_code:
        print(year.book_year)


