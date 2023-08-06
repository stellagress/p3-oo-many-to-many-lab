class Author:
    all = []

    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")

        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")

        if not isinstance(date, str):
            raise Exception("Date must be string type")

        if not isinstance(royalties, int):
            raise Exception("Royalties must be integer type")

    @classmethod
    def contracts_by_date(cls, date=None): 
        if date is None:
            return sorted(cls.all, key=lambda contract: contract.date)
        return [contract for contract in cls.all if contract.date == date]


    # @classmethod
    # def contracts_by_date(cls, date=None):
    #     return [contract for contract in cls.all if contract.date == date]





# class Author:
#     all = []

#     def __init__(self, name):
#         self.name = name

#     def contracts(self):
#         return [contract for contract in Contract.all if contract.author == self]

#     def books(self):
#         return [contract.book for contract in self.contracts()]

#     def sign_contract(self, book, date, royalties):
#         return Contract(self, book, date, royalties)

#     def total_royalties(self):
#         return sum(contract.royalties for contract in self.contracts())


# class Book:
#     all = []

#     def __init__(self, title):
#         self.title = title


# class Contract:
#     all = []

#     def __init__(self, author, book, date, royalties):
#         self.author = author
#         self.book = book
#         self.date = date
#         self.royalties = royalties
#         Contract.all.append(self)

#         if not isinstance(author, Author):
#             raise Exception("Author must be an instance of Author class")

#         if not isinstance(book, Book):
#             raise Exception("Book must be an instance of Book class")

#         if not isinstance(date, str):
#             raise Exception("Date must be string type")

#         if not isinstance(royalties, int):
#             raise Exception("Royalties must be integer type")






