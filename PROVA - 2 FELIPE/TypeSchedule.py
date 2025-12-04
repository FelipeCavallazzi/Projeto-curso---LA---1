from schedule import Schedule

class TypeSchedule(Schedule):

    def __init__(self, data, codDoctor, type, description: str):
        super(). __init__ (self, data, codDoctor, type)
        self.__description = description