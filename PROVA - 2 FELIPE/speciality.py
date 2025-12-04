from doctors import Doctors

class MedicalSpeciality(Doctors):

    def __init__(self, name, codDoctor, codSpeciality, crm, phone, email, medicalSpeciality: str):
        super().__init__(name, codDoctor, codSpeciality, crm, phone, email)
        self.__medicalSpeciality = medicalSpeciality

    @property
    def medicalSpeciality(self):
        return self.__medicalSpeciality

    @medicalSpeciality.setter
    def medicalSpeciality(self, medicalSpeciality: str):
        self.__medicalSpeciality = medicalSpeciality

    # Método

    def __str__(self):
        return self.medicalSpeciality



