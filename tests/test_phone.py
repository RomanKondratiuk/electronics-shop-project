"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest

from src.phone import Phone


@pytest.fixture
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def tests__str__(phone_1):
    """test for __str__"""
    assert str(phone_1) == 'iPhone 14'


def test__repr__(phone_1):
    """test for __repr__"""
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_quantity_of_sim(phone_1):
    """test for quantity_of_sim"""
    assert phone_1.quantity_of_sim == 2

