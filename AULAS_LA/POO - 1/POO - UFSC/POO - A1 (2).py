#Baseado no "Diagrama de classes no moodle"

#Classes
class Client():
    def __init__(self, name, cpf, address, address_number, address_complement, dt_birth, phone, email):
        #Atributes private
        self.__name = name #Underscore pra deixar a palavra reservada
        self.__cpf = cpf
        self.__address = address
        self.__address_number = address_number
        self.__address_complement = address_complement
        self.__dt_birth = dt_birth
        self.__phone = phone
        self.__email = email

    #Getters (recupera e grava o atributo)
    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def address(self):
        return self.__address

    @property
    def address_number(self):
        return self.__address_number

    @property
    def address_complement(self):
        return self.__address_complement

    @property
    def dt_birth(self):
        return self.__dt_birth

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    #Setters (registra os valores dos atributos)
    @name.setter
    def name(self, name):
        self.__name = name

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @address.setter
    def address(self, address):
        self.__address = address

    @address_number.setter
    def address_number(self, address_number):
        self.__address_number = address_number

    @address_complement.setter
    def address_complement(self, address_complement):
        self.__address_complement = address_complement

    @dt_birth.setter
    def dt_birth(self, dt_birth):
        self.__dt_birth = dt_birth

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email

    #Functions
    def __str__(self):
        f"Name: {name}"




#Instances
client = Client("Joao" ,  2345678901 ,
                "Rua das orquideas" , 59 , "Apto 1001" ,
                "12/04/2007" , "48 999576388" , "joao@gmail.com")

#Exit
print(client.name)

