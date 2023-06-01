"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price_1(item1):
    """test for instance 'item1'"""
    assert item1.calculate_total_price() == 200000


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price_2(item2):
    """test for instance 'item2'"""
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_string_to_number():
    """tests for func 'string_to_number'"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    """test for list"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.name = 'Смартфон'
    item2 = Item.name = 'Ноутбук'
    item3 = Item.name = 'Кабель'
    item4 = Item.name = 'Мышка'
    item5 = Item.name = 'Клавиатура'

    assert item1 == 'Смартфон'
    assert item2 == 'Ноутбук'
    assert item3 == 'Кабель'
    assert item4 == 'Мышка'
    assert item5 == 'Клавиатура'


@pytest.fixture
def item3():
    return Item('Смартфон', 10000, 20)


def test__repr__(item3):
    """test for __repr__"""
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__(item3):
    """test for __str__"""
    assert str(item1) == 'Смартфон'


