# Library Book Management System


# Node for Linked List
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None


# Linked List for Book Records
class BookList:
    def __init__(self):
        self.head = None

    # Insert new book
    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"Book '{title}' added successfully.")

    # Delete a book by ID
    def deleteBook(self, book_id):
        temp = self.head
        prev = None
        while temp:
            if temp.book_id == book_id:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Book '{temp.title}' deleted successfully.")
                return
            prev = temp
            temp = temp.next
        print("Book not found!")

    # Search for a book
    def searchBook(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                print(f"Found Book - ID: {temp.book_id}, Title: {temp.title}, Author: {temp.author}, Status: {temp.status}")
                return temp
            temp = temp.next
        print("Book not found!")
        return None

    # Display all books
    def displayBooks(self):
        temp = self.head
        if not temp:
            print("No books in the library.")
            return
        print("\nCurrent Book List:")
        print("-" * 50)
        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | Author: {temp.author} | Status: {temp.status}")
            temp = temp.next
        print("-" * 50)


# Stack for Transaction Management
class TransactionStack:
    def __init__(self):
        self.stack = []

    def push(self, transaction):
        self.stack.append(transaction)

    def pop(self):
        if not self.stack:
            print("No transaction to undo.")
            return None
        return self.stack.pop()

    def viewTransactions(self):
        if not self.stack:
            print("No transactions yet.")
            return
        print("\nTransaction History:")
        for i, t in enumerate(reversed(self.stack), 1):
            print(f"{i}. {t}")


# Transaction Management System
class LibrarySystem:
    def __init__(self):
        self.book_list = BookList()
        self.transactions = TransactionStack()

    def issueBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Available":
            book.status = "Issued"
            self.transactions.push(("issue", book_id))
            print(f"Book '{book.title}' has been issued.")
        elif book:
            print("Book already issued!")

    def returnBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transactions.push(("return", book_id))
            print(f"Book '{book.title}' has been returned.")
        elif book:
            print("Book was not issued!")

    def undoTransaction(self):
        transaction = self.transactions.pop()
        if not transaction:
            return
        action, book_id = transaction
        book = self.book_list.searchBook(book_id)
        if not book:
            print("Book record not found for undo.")
            return

        if action == "issue":
            book.status = "Available"
            print(f"Undo: Book '{book.title}' is now available again.")
        elif action == "return":
            book.status = "Issued"
            print(f"Undo: Book '{book.title}' is marked as issued again.")

    def viewTransactions(self):
        self.transactions.viewTransactions()


# Demo / Testing the system

if __name__ == "__main__":
    system = LibrarySystem()

    # Insert sample books
    system.book_list.insertBook(101, "C Programming", "Dennis Ritchie")
    system.book_list.insertBook(102, "Data Structures", "Narasimha Karumanchi")
    system.book_list.insertBook(103, "Algorithms", "CLRS")

    # Display all books
    system.book_list.displayBooks()

    # Issue and Return
    system.issueBook(101)
    system.issueBook(102)
    system.returnBook(101)
    system.viewTransactions()

    # Undo last action
    system.undoTransaction()
    system.book_list.displayBooks()
