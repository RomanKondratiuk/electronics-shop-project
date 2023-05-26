

import csv

from poetry.console.commands import self


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name
        else:
             print("Длина наименования товара превышает 10 символов.")


    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
          """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
         класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        #  """
        cls.all.clear()
        with open("/Users/romankondratiuk/Desktop/electronics-shop-project/src/items.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.all.append(row)
            return f' в файле {cls.all} записей с данными по товарам'


                # cls.all.append(row)

           # print(f"в файле {len(cls.all)} записей с данными по товарам")


    @staticmethod
    def string_to_number(number):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(number))


