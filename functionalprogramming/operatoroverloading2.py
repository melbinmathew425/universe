class Book:
    def __init__(paperback,pages):
        paperback.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return str(self.pages)
b1=Book(120)
b2=Book(200)
b3=Book(180)
print(b1+b2+b3)