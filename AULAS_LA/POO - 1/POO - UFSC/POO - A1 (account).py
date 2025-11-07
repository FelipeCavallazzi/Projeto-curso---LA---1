#Class
class CheckingAccount():
    #Constructor
    def __init__(self, account_number, account_dig, balance, agency, agency_dig, code):
        # super class
        super().__init__(agency, agency_dig, code)
        # atributes privates
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__balance = balance

    #Getters
    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_dig(self):
        return self.__account_dig

    @property
    def balance(self):
        return self.__balance

    @property
    def agency(self):
        return self._Account__agency  # acessando atributo herdado da superclasse

    @property
    def code(self):
        return self._Account__code

    @property
    def account(self):
        return self._Account__account

    #Setters
    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @agency.setter
    def agency(self, agency):
        self._Account__agency = agency

    @code.setter
    def code(self, code):
        self._Account__code = code

    @account.setter
    def account(self, account):
        self._Account__account = account

    #show account information
    def __str__(self):
        return(
            f"Número da conta: {self.__account_number}-{self.agency_dig}\n"
            f"Código do banco: {self.__balance}"
        )

    def update_balance(self):
        self.__balance *= 1.01

#Instances
checkingAccount=CheckingAccount(27346, 3, 456, 1234, 5, )
new_balance = checkingAccount.update_balance()

#Exit
print(checkingAccount)
print(new_balance)
