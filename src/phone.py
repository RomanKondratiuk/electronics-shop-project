from src.item import Item


class Phone(Item):
    """
    Дочерний класс от 'item' , который имеет  атрибут, содержащий количество поддерживаемых сим-карт
    """
    def __init__(self, name, price, quantity, quantity_of_sim):
        super().__init__(name, price, quantity)
        self.__quantity_of_sim = quantity_of_sim

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return "Число не является атрибутом класссов"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__quantity_of_sim})"

    @property
    def quantity_of_sim(self):
        return self.__quantity_of_sim

    @quantity_of_sim.setter
    def quantity_of_sim(self, quantity_of_sim):
        if isinstance(quantity_of_sim, int) and quantity_of_sim > 0:
            self.__quantity_of_sim = quantity_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")






