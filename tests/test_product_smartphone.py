import pytest


def test_product_smartphone_init(smartphone_1):
    """Тест инициализации класса Product"""
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_product_smartphone_add_success(smartphone_1, smartphone_2):
    """Тест на определение суммарной стоимости товаров с использованием фикстур для двух объектов класса Smartphone"""
    # Вызов метода __add__ из класса Smartphone для суммирования стоимости товаров экземпляров класса
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_product_smartphone_add_other_class(smartphone_1):
    """Тест на корректную работу метода `__add__`, если новый объект другого класса"""
    with pytest.raises(TypeError):
        smartphone_1 + 1
