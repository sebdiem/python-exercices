from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Book:
    title: str
    author: str
    isbn: str

    is_issued: bool = False

    def issue_book(self):
        self.is_issued = True

    def return_book(self):
        self.is_issued = False


@dataclass
class Member:
    id: str
    name: str
    issued_books: List[str] = field(default_factory=list)

    is_issued: bool = False

    def borrow_book(self, book_isbn: str):
        self.issued_books.append(book_isbn)

    def return_book(self, book_isbn: str):
        self.issued_books.remove(book_isbn)


@dataclass
class Library:
    books: Dict[str, Book] = field(default_factory=dict)
    members: Dict[str, Member] = field(default_factory=dict)

    def get_book(self, book_isbn: str) -> Book:
        return self.books[book_isbn]

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def remove_book(self, book_isbn: str):
        self.books = [b for b in self.books if b.isbn != book_isbn]

    def register_member(self, member: Member):
        self.members[member.id] = member

    def issue_book_to_member(self, book_isbn: str, member_id: str):
        self.members[member_id].borrow_book(book_isbn)
        self.get_book(book_isbn).issue_book()

    def return_book_from_member(self, book_isbn: str, member_id: str):
        self.members[member_id].return_book(book_isbn)
        self.get_book(book_isbn).return_book()


def library_factory() -> Library:
    library = Library()

    book1 = Book(title="The Great Gatsby",
                 author="F. Scott Fitzgerald", isbn="9780743273565")
    book2 = Book(title="Moby Dick", author="Herman Melville",
                 isbn="9781503280786")
    book3 = Book(title="1984", author="George Orwell", isbn="9780451524935")
    book4 = Book(title="To Kill a Mockingbird",
                 author="Harper Lee", isbn="9780061120084")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    member1 = Member(id="M001", name="Alice Smith")
    member2 = Member(id="M002", name="Bob Johnson")
    member3 = Member(id="M003", name="Charlie Brown")

    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)

    return library


if __name__ == "__main__":
    print(library_factory())
