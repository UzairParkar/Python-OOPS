class Book:
    def __init__(self, id=0, title=None, author=None , copies = 0):
        self.id = id
        self.title  = title
        self.author = author 
        self.copies = copies

    def __str__(self):
        status = 'Available' if self.copies > 0 else 'Not Available'
        return f'ID: {self.id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}, Status: {status}'
        




class Library:
    def __init__(self,name):
        self.Library_name  = name
        self.books = []

    def add_books(self,title,author,copies=1): 
        for book in self.books:
            if book.title == title and book.author == author:
                book.copies += copies
                print('updated copies')
                return
            

        new_book = Book(
            id = len(self.books) +1,
            title = title, 
            author = author,
            copies = copies
        )
        self.books.append(new_book)
            
        print(f'Book {title} created successfully')

    def display_books(self):
        if not self.books:
            print('No Books Available in the library')
        else:
            print(self.Library_name)
            for book in self.books:
                print(book)

    def borrow_book(self,id):
        for book in self.books:
            if book.id == id:
                if book.copies > 0:
                    book.copies -= 1
                    print(f'{book.title} borrowed successfully')
                else:
                    print(f'{book.title} is not available')


    def return_book(self,id):
        for book in self.books:
            if book.id == id:
                book.copies += 1
                print(f'{book.title} returned successfully')
            else:
                print(f'{book.title} not found')
                return

library = Library('Eternal Library')

library.Library_Name = 'Test library'

library.add_books(title='HBP',author='JK',copies=14)
library.borrow_book(1)
library.display_books()
library.return_book(1)


                 







