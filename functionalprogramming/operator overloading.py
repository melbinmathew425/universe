class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(first, second):
        return Book(first.pages+second.pages)
    def __str__(self):
        return str(self.pages)
b1=Book(100)
b2=Book(200)
print(b1+b2)