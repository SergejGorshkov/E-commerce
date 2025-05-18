import pytest

from src.category import Category
from src.product import Product
from src.exceptions import ZeroQuantityProduct


def test_product_init(some_product):
    """Тест инициализации класса Product"""
    assert some_product.name == "Motorola"
    assert some_product.description == "Телефон - легенда"
    assert some_product.price == 1000.0
    assert some_product.quantity == 10


def test_product_init_zero_quantity():
    """Тест инициализации класса Product, если передано неверное количество товара"""
    with pytest.raises(ZeroQuantityProduct):
        Product(name="Motorola", description="Телефон - легенда", price=1000.0, quantity=0)

    with pytest.raises(ZeroQuantityProduct):
        Product(name="Motorola", description="Телефон - легенда", price=1000.0, quantity=1.5)

    with pytest.raises(ZeroQuantityProduct):
        Product(name="Motorola", description="Телефон - легенда", price=1000.0, quantity="10")


def test_new_product_classmethod_if_new(first_category):
    """Тест на корректную работу классметода new_product, если товар новый"""
    new_data = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
                "price": 185000.0,
                "quantity": 5}
    new_product = Product.new_product(new_data, first_category)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 185000.0
    assert new_product.quantity == 5


def test_new_product_classmethod_if_exist(capsys, some_product):
    """Тест на корректную работу классметода new_product, если такой товар уже есть"""
    new_data = {"name": "Motorola", "description": "Телефон - легенда", "price": 1500.0, "quantity": 3}

    test_category = Category(name="Смартфоны",
                             description="Смартфоны - это весело и удобно!",
                             products=[some_product])
    Product.new_product(new_data, test_category)
    message = capsys.readouterr()
    assert ("При попытке добавления нового товара 'Motorola' в указанной категории обнаружен аналогичный товар. "
            "Количество товаров в указанной категории было увеличено. Новый товар не был добавлен.") in message.out

    assert some_product.quantity == 13  # Кол-во товара увеличилось на 3
    assert some_product.price == 1500.0  # Цена товара заменилась на большее значение new_data["price"]


def test_product_str(some_product):
    """Тест на строковое представление объектов класса Product (с использованием фикстуры some_product)"""
    # Вызов метода __str__ из класса Product для отображения информации об экземпляре класса
    assert str(some_product) == "Motorola, 1000.0 руб. Остаток: 10 шт."


def test_product_add_success(some_product, some_product_2):
    """Тест на определение суммарной стоимости товаров с использованием фикстур для двух объектов класса Product"""
    # Вызов метода __add__ из класса Product для суммирования стоимости товаров экземпляров класса
    assert some_product + some_product_2 == 510000.0


def test_product_add_other_class(some_product):
    """Тест на корректную работу метода `__add__`, если новый объект другого класса"""
    with pytest.raises(TypeError):
        some_product + 1
