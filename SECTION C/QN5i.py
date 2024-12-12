
# 5(i)
class Book:
    def _init_(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = 678

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


book = Book("Python Programming", "Sarah Orishaba", 350)
book.display_info()
# 5(ii)
class EBook(Book):
    def _init_(self, title, author, pages, file_size):
        super()._init_(title, author, pages)
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size}MB")

# 5(iii)
ebook = EBook("Python Programming", "Sarah Orishaba" )
ebook.display_info()
