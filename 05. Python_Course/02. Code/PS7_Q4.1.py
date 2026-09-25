# Create a class Book with attributes title and author .
# Implement __str__() so that printing the object displays "Title by Author" .
# Implement __len__() so that len(book) returns the length of the title.
# Create two Book objects and test these methods.
# Solution ==>

class Book:
    def __init__(self, title, author):
       self.Title = title
       self.Author = author
    
    def __len__ (self):
        return len(self.Title)

    def __str__(self):
        return f"{self.Title} by {self.Author}"
    

B1 = Book("Wings of Fire", "A.P.J Kalam")
B2 = Book("A Brief History of Time", "Stephen Hawkings")

print(str(B1))
print(len(B1))


print(str(B2))
print(len(B2))

