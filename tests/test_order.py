import pytest
from src.order import Order


def test_add_product_success(some_product):
    """Тест на корректное получение информации о товаре в заказе (наименование, количество и итоговая стоимость)"""
    assert Order.add_product(some_product, 2) == 'Товар в заказе: Motorola, количество: 2, итоговая стоимость: 2000.0.'


def test_add_product_if_other_class(first_category, some_product):
    """Тест на корректную работу метода `add_product`, если переданный объект другого класса или неверно указано
    количество товара"""
    with pytest.raises(TypeError):
        Order.add_product(first_category, 2)
    with pytest.raises(TypeError):
        Order.add_product(some_product, 0)
    with pytest.raises(TypeError):
        Order.add_product(some_product, -1)
    with pytest.raises(TypeError):
        Order.add_product(some_product, 1.5)
