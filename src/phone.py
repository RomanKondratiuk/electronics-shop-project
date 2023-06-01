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







# item_1 = Item("iPhone 13", 100_000, 7)
# phone_1 = Phone("iPhone 14", 120_000, 5, 2)
# phone_2 = Phone("iPhone 12", 80_000, 3, 2)
#
# total_quantity = item_1 + phone_1
# #total_quantity = phone_1 + phone_2
# #total_quantity = phone_1 + 8
#
#
#print(total_quantity)