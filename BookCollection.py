# BookCollection.py

from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def getNumberOfBooks(self):
        count = 0
        book = self.head
        while book is not None:
            count += 1
            book = book.getNext()
        return count
 
    def insertBook(self, book):
        book_node = BookCollectionNode(book)

        # "book" will be the first value ()
        if self.head is None or self.head.getData() > book: # smaller should come first
            book_node.setNext(self.head)
            self.head = book_node
        # there are multiple data that book needs to be compared with
        else:
            current_book = self.head
            while current_book.getNext() is not None:
                if current_book.getNext().getData() > book:
                    break
                current_book = current_book.getNext()
            
            book_node.setNext(current_book.getNext())
            current_book.setNext(book_node)


    def getBooksByAuthor(self, author):
        result = []
        author_name = author.lower()
        book_examined = self.head
        
        while book_examined is not None:
            book_author = book_examined.getData().getAuthor().lower()
            if book_author == author_name:
                result.append(book_examined.getData().getBookDetails())
            book_examined = book_examined.getNext()
        
        if result:
            authors_book = "\n".join(result) + "\n"
        else: # no books in the list
            authors_book = ""
        return authors_book


    def getAllBooksInCollection(self):
        result = []
        book = self.head

        while book is not None:
            book_data = book.getData().getBookDetails()
            result.append(book_data)
            book = book.getNext()

        if result:
            all_books = "\n".join(result) + "\n"
        else:
            all_books = ""
        return all_books


    def removeAuthor(self, author):
        author_name = author.lower()
        book_examined = self.head
        previous_book = None

        while book_examined is not None:
            book_author = book_examined.getData().getAuthor().lower()

            if book_author == author_name: # if a book is by a certain author

                if previous_book is None: # the first book in the list to be removed
                    self.head = book_examined.getNext()
                    # set the next book to the first book in the list

                else: # remove a book in the middle or end of the list
                    previous_book.setNext(book_examined.getNext())
                    # connect (set) previous_book's next book
                    # with
                    # book_examined's next book

                book_examined = book_examined.getNext()
                # move to the next book

            else: # if a book is not by a certain author
                previous_book = book_examined
                book_examined = book_examined.getNext()
                # move (set) each value to the next one


    def recursiveSearchTitle(self, title, bookNode):
        if bookNode is None:
            return False
        
        title_examined = bookNode.getData().getTitle().lower()
        search_title = title.lower()

        if title_examined == search_title:
            return True
        
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())
