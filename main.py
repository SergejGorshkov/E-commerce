import os
from pprint import pprint

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json_file

PATH = os.path.join(os.path.dirname(__file__), "data", "products.json")  # Путь к JSON-файлу

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                         "функций для удобства жизни",
                         [product1, product2, product3])


    print(category1.products)  # Список из строк ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n', ...]
    print(category1.product_count)  # 3
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)  # Добавление нового товара в категорию `category1`
    print(category1.products)  # Т.к. есть геттер `products` в `category.py`, можем вывести приватный список продуктов
    print(category1.product_count)  # 4

    new_same_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 185000.0,
         "quantity": 5}, category1)

    #Т.к. товар new_same_product уже есть в указанной категории, объект был создан пустым. При этом были изменены атрибуты
    # уже имеющегося товара (количество, цена (при необходимости))
    print(new_same_product.name)  # None
    print(new_same_product.description)  # None
    print(new_same_product.price)  # None
    print(new_same_product.quantity)  # None
    print(product1.quantity)  # 10 (кол-во товара увеличилось)
    print(product1.price)  # 185000.0 (цена товара увеличилась)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy A25", "description": "256GB, Серый цвет, 200MP камера", "price": 28000.0,
         "quantity": 3}, category1)

    # Т.к. товара new_product еще нет в указанной категории, объект был создан с переданными параметрами
    print(new_product.name)  # Samsung Galaxy A25
    print(new_product.description)  # 256GB, Серый цвет, 200MP камера
    print(new_product.price)  # 28000.0
    print(new_product.quantity)  # 3

    new_product.price = 800  # Задаем новую меньшую цену
    print(new_product.price)  # 800

    new_product.price = -100  # Цена не должна быть нулевая или отрицательная
    print(new_product.price)  # 800
    new_product.price = 0  # Цена не должна быть нулевая или отрицательная
    print(new_product.price)  # 800
