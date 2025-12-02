# Account Super Class

# Classes
class Account:
    # Constructor
    def __init__(self, agency, agency_dig, code):
        # Atributes Privates
        self.__agency=agency
        self.__agency_dig=agency_dig
        self.__code=code

    # Getters

    @property
    def agency(self):
        return self.__agency

    @property
    def agency_dig(self):
        return self.__agency_dig

    @property
    def code(self):
        return self.__code

    # Setters

    @agency.setter
    def agency(self, agency):
        self.__agency = agency

    @agency_dig.setter
    def agency_dig(self, agency_dig):
        self.__agency_dig = agency_dig

    @code.setter
    def code(self, code):
        self.__code = code

    # Show Account Informations
    def __str__(self):
        return (
            f"Agencia: {self.__agency}-{self.agency_dig}\n"
            f"Código do banco: {self.__code}"
        )

    def update_balance(self):
        print("Valor atualizado!")

# Instances
account=Account(1234, 5, 131)

# Exit
print(account)