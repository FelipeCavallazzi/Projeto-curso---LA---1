from schedule import Schedule

class Appointments(Schedule):

    def __init__(self, data, codDoctor, type, cod: int, status: str):
        super().__init__(data, codDoctor, type)
        self.__cod = cod
        self.__status = status

        @property
        def cod(self):
            return self.__cod

        @cod.setter
        def cod(self, cod):
            self.__cod = cod

        @property
        def status(self):
            return self.__status

        @status.setter
        def status(self, status):
            self.__status = status

        # Método

        # Métodos
        def update_schedule(self):
            type = int(input("Insira o tipo de agenda: "))
            codDoctor = int(input("Insira o código do médico: "))
            data = input("Insira a data: ")
            cod = int(input("Insira o código: "))
            status = input("Insira o status: ")

            self.type = type
            self.codDoctor = codDoctor
            self.data = data
            self.cod = cod
            return type, codDoctor, data, cod, status
