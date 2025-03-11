# Book

class Book:

    def __init__(self, title="", author="", year=None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year

    def getBookDetails(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
# Book’s author (in lexicographical / alphabetical order).
# In the event of a tie (several books are written by the same author),
# the published year will be used to determine the Book object’s place in the Ordered Linked List.
# If the author and year published are the same,
# then the Book’s title (lexicographical / alphabetical order)
# will be used to determine the Book object’s place in the Ordered Linked List.

    def __gt__(self, rhs):
        if self.author > rhs.author:
            return True
        elif self.author < rhs.author:
            return False
        else: # author is the same
            if self.year > rhs.year:
                return True
            elif self.year < rhs.year:
                return False
            else: # year is also the same
                if self.title > rhs.title:
                    return True
                elif self.title < rhs.title:
                    return False
