class Users:

    # 1. Constructor (com atributos privados)
    def __init__(self, cpf, name, phone, email, password, address, addressNumber, dtBirth, typeUser, userName):
        """Inicializa um novo objeto User."""
        self.__cpf = cpf
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__password = password
        self.__address = address
        self.__addressNumber = addressNumber
        self.__dtBirth = dtBirth
        self.__typeUser = typeUser
        self.__userName = userName

    # Getters
        @property
        def name(self):
            """Getter para o nome."""
            return self.__name

        @property
        def phone(self):
            """Getter para o telefone."""
            return self.__phone

        @property
        def email(self):
            """Getter para o email."""
            return self.__email

        @property
        def cpf(self):
            return self.__cpf

        @property
        def password(self):
            return self.__password

        @property
        def address(self):
            return self.__address

        @property
        def addressNumber(self):
            return self.__addressNumber

        @property
        def typeUser(self):
            return self.__typeUser

        @property
        def userName(self):
            return self.__userName

    # Setters
        @name.setter
        def name(self, name):
            self.__name = name

        @phone.setter
        def phone(self, phone):
            self.__phone = phone

        @email.setter
        def email(self, email):
            self.__email = email

        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf

        @password.setter
        def password(self, password):
            self.__password = password

        @address.setter
        def address(self, address):
            self.__address = address

        @addressNumber.setter
        def addressNumber(self, addressNumber):
            self.__addressNumber = addressNumber

        @dtBirth.setter
        def dtBirth(self, dtBirth):
            self.__dtBirth = dtBirth

        @typeUser.setter
        def typeUser(self, typeUser):
            self.__typeUser = typeUser

        @userName.setter
        def userName(self, userName):
            self.__userName = userName

    # Métodos

    def updatePerson(self):
        print("\n--- Update User ---")

        cpf = input("Insira seu cpf: ")
        self.cpf = cpf

        name = input("Insira seu nome: ")
        while name.strip() == "":
            print("Erro: O nome não pode ser vazio.")
            name = input("Insira seu nome: ")
        self.name = name

        phone = input("Insira seu telefone: ")
        while not phone.isdigit():
            print("Erro: O telefone deve conter somente números.")
            phone = input("Insira um telefone válido: ")
        while phone.strip() == "":
            print("Erro: O telefone não pode ser vazio.")
            phone = input("Insira um telefone válido: ")
        self.phone = phone

        email = input("Insira seu email: ")
        while not ("@" in email and "." in email):
            print("Erro: Email inválido.")
            email = input("Insira um email válido: ")
        self.email = email

        password = input("Insira sua senha: ")
        while password == "":
            print("\nSenha vazia e inválida!")
            password = input("Insira senha válida: ")
        self.password = password

    def __str__(self):
        return str