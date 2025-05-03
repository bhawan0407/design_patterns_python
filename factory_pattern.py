from abc import ABC, abstractmethod

# Abstract Product
class LibraryItem(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Concrete Products
class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        self.title = title
        self.issue_number = issue_number

    def get_details(self):
        return f"Magazine: {self.title}, Issue: {self.issue_number}"

class DVD(LibraryItem):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_details(self):
        return f"DVD: {self.title}, Duration: {self.duration} minutes"

# Factory
class LibraryItemFactory:
    @staticmethod
    def create_item(item_type, *args):
        if item_type == "book":
            return Book(*args)
        elif item_type == "magazine":
            return Magazine(*args)
        elif item_type == "dvd":
            return DVD(*args)
        else:
            raise ValueError(f"Unknown item type: {item_type}")

# Client Code
if __name__ == "__main__":
    factory = LibraryItemFactory()

    book = factory.create_item("book", "The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    magazine = factory.create_item("magazine", "National Geographic", "2023-10")
    dvd = factory.create_item("dvd", "Inception", 148)

    print(book.get_details())
    print(magazine.get_details())
    print(dvd.get_details())