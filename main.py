class Product:
    def __init__(self, name, quantity, status):
        self.__name = name
        self.__quantity = quantity
        self.__status = status

    @property
    def name(self):
        return self.__name


    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self.__quantity = value
        else:
            print("Xatolik")

    @property
    def status(self):
        return self.__status


    @status.setter
    def status(self):
        if self.__quantity >= 0:
            self.__status = "mavjud emas"
        else:
