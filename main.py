import os

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator

# from pprint import pprint

# from src.utils import create_objects_from_json, read_json_file

PATH = os.path.join(os.path.dirname(__file__), "data", "products.json")  # Путь к JSON-файлу

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                         "функций для удобства жизни",
                         [product1, product2, product3])

    print(str(category1))  # Смартфоны, количество продуктов: 27 шт.
    print(category1.products)  # ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n',
    # 'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n', 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n']

    print(product1 + product2)  # 2580000.0
    print(product1 + product3)  # 1334000.0
    print(product2 + product3)  # 2114000.0

    iterator = ProductIterator(category1)  # Создание итератора с товарами для категории `category1`
    for product in iterator:  # Последовательно вызываются методы __iter__ и __next__ из класса ProductIterator
        print(product)  # Т.к. для класса Product написан __str__, при выводе экземпляра класса возвращается строка,
        # форма которой описана в методе __str__ класса Product

############################################################################################################
# Ниже - проверки из предыдущих ДЗ. После завершения проекта удалить

    # print(category1.products)  # Список из строк ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n', ...]
    # print(category1.product_count)  # 3
    # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    # category1.add_product(product4)  # Добавление нового товара в категорию `category1`
    # print(category1.products)  # Т.к. есть геттер products в category.py, можем вывести приватный список продуктов
    # print(category1.product_count)  # 4
    #
    # new_same_product = Product.new_product(
    #     {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 185000.0,
    #      "quantity": 5}, category1)
    #
    # # Т.к. товар new_same_product уже есть в указанной категории, объект был создан пустым. При этом были изменены
    # # атрибуты уже имеющегося товара (количество, цена (при необходимости))
    # print(new_same_product.name)  # None
    #
    # print(product1.quantity)  # 10 (кол-во товара увеличилось)
    # print(product1.price)  # 185000.0 (цена товара увеличилась)
    #
    # new_product = Product.new_product(
    #     {"name": "Samsung Galaxy A25", "description": "256GB, Серый цвет, 200MP камера", "price": 28000.0,
    #      "quantity": 3}, category1)
    #
    # # Т.к. товара new_product еще нет в указанной категории, объект был создан с переданными параметрами
    # print(new_product.name)  # Samsung Galaxy A25
    # print(new_product.description)  # 256GB, Серый цвет, 200MP камера
    # print(new_product.price)  # 28000.0
    # print(new_product.quantity)  # 3
    #
    # new_product.price = 800  # Задаем новую меньшую цену
    # print(new_product.price)  # 800
    #
    # new_product.price = -100  # Цена не должна быть нулевая или отрицательная
    # print(new_product.price)  # 800
    # new_product.price = 0  # Цена не должна быть нулевая или отрицательная
    # print(new_product.price)  # 800
