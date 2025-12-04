from doctors import Doctors

class Schedule:

    def __init__(self, data: str, codDoctor: int, type: int):
        self.__data = data
        self.__codDoctor = codDoctor
        self.__type = type

    # Getters E Setters
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def codDoctor(self):
        return self.__codDoctor

    @codDoctor.setter
    def codDoctor(self, codDoctor: int):
        self.__codDoctor = codDoctor

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    # Métodos
    def update_schedule(self):
        type = int(input("Insira o tipo de agenda: "))
        codDoctor = int(input("Insira o código do médico: "))
        data = input("Insira a data: ")
        self.__type = type
        self.__codDoctor = codDoctor
        self.__data = data
        return type, codDoctor, data

s = Schedule("29042007", 1, 2)

print(s.update_schedule())