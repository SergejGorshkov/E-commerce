import pytest


def test_product_lawngrass_init(lawngrass_1):
    """Тест инициализации класса LawnGrass"""
    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.quantity == 20
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"


def test_product_lawngrass_add_success(lawngrass_1, lawngrass_2):
    """Тест на определение суммарной стоимости товаров с использованием фикстур для двух объектов класса LawnGrass"""
    # Вызов метода __add__ из класса LawnGrass для суммирования стоимости товаров экземпляров класса
    assert lawngrass_1 + lawngrass_2 == 16750.0


def test_product_lawngrass_add_other_class(lawngrass_1):
    """Тест на корректную работу метода `__add__`, если новый объект другого класса"""
    with pytest.raises(TypeError):
        lawngrass_1 + 1
