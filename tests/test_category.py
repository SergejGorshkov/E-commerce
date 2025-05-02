import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    """Тест инициализации класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны - это весело и удобно!"
    assert len(first_category.products) == 2

    assert len(second_category.products) == 1

    assert Category.category_count == 2  # Количество категорий
    assert Category.product_count == 3  # Количество товаров во всех категориях

    # Количество категорий для обоих объектов класса должно быть одинаковым и равным сумме всех категорий
    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_add_product_success(first_category):
    """Тест на корректную работу метода `add_product`"""
    test_product = Product("Samsung Galaxy A25", "256GB, Серый цвет, 200MP камера", 28000.0, 3)
    first_category.add_product(test_product)
    assert first_category.products == ['Motorola, 1000.0 руб. Остаток: 10 шт.\n',
                                       'Samsung, 2000.0 руб. Остаток: 5 шт.\n',
                                       'Samsung Galaxy A25, 28000.0 руб. Остаток: 3 шт.\n']


def test_add_product_empty_new_product(first_category):
    """Тест на корректную работу метода `add_product`, если новый объект пустой"""
    test_product = None
    with pytest.raises(TypeError):
        first_category.add_product(test_product)


def test_category_str(second_category):
    """Тест на строковое представление объектов класса Category (с использованием фикстуры second_category)"""
    # Вызов метода __str__ из класса Category для отображения информации об экземпляре класса
    assert str(second_category) == "Телевизоры, количество продуктов: 2 шт."


def test_product_iterator(product_iterator):
    """Тест работы итератора из класса ProductIterator с фикстурой product_iterator"""
    iter(product_iterator)  # Переопределение метода __iter__, чтобы индекс для перебора последовательности объектов
    # класса ProductIterator обнулился

    assert product_iterator.index == 0  # Проверка, что первоначальное значение индекса = 0

    # В product_iterator указана фикстура first_category с двумя товарами
    assert next(product_iterator).name == "Motorola"  # Проверка, что имя экземпляра класса Product соответствует
    # названию первого товара
    assert next(product_iterator).name == "Samsung"  # Проверка, что имя экземпляра класса Product соответствует
    # названию второго товара

    with pytest.raises(StopIteration):  # Проверка корректного завершения работы итератора
        next(product_iterator)
