# Classe
class Book:
    def __init__(self, id_book, title, author, isbn, quantity):
        self.id_book = 0
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.status = True

    def get_book_details(self):
        book_details = f"\nTítulo: {self.title.title()}\nAutor: {self.author.title()}\nISBN: {self.isbn}\nQuantity: {self.quantity}"
        return book_details.title()

    def update_status(self):
        if self.quantity == 0:
            self.status = False


    def check_availability(self):
        #EMPAQUEI
        if self.status == False:
            check_disponivel = ("Livro indisponível.")
        else:
            check_disponivel = ("Livro disponível!")



book_one = Book(1, "cacau", "Jorge Amado", "2004", 20)

print(book_one.get_book_details())






