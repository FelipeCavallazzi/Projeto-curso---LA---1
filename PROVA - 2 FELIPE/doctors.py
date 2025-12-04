class Doctors:

    def __init__(self, name, codDoctor: int, codSpeciality: int, crm: int, phone, email):
        self.__name = name
        self.__codDoctor = codDoctor
        self.__codSpeciality = codSpeciality
        self.__crm = crm
        self.__phone = phone
        self.__email = email

    # Getters e Setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def codDoctor(self):
        return self.__codDoctor

    @codDoctor.setter
    def codDoctor(self, codDoctor):
        self.__codDoctor = codDoctor

    @property
    def codSpeciality(self):
        return self.__codSpeciality

    @codSpeciality.setter
    def codSpeciality(self, codSpeciality):
        self.__codSpeciality = codSpeciality

    @property
    def crm(self):
        return self.__crm

    @crm.setter
    def crm(self, crm):
        self.__crm = crm

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return self.name, self.codDoctor, self.codSpeciality, self.crm, self.phone, self.email
