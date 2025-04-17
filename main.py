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

    print(product1.name)  # Samsung Galaxy S23 Ultra
    print(product1.description)  # 256GB, Серый цвет, 200MP камера
    print(product1.price)  # 180000.0
    print(product1.quantity)  # 5

    print(product2.name)  # Iphone 15
    print(product2.description)  # 512GB, Gray space
    print(product2.price)  # 210000.0
    print(product2.quantity)  # 8

    print(product3.name)  # Xiaomi Redmi Note 11
    print(product3.description)  # 1024GB, Синий
    print(product3.price)  # 31000.0
    print(product3.quantity)  # 14

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                         "функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")  # True
    print(
        category1.description)  # Смартфоны, как средство не только коммуникации, но и получения дополнительных функций
    # для удобства жизни
    print(len(category1.products))  # 3
    print(category1.category_count)  # 1
    print(category1.product_count)  # 3

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим "
                         "другом и помощником",
                         [product4])

    print(category2.name)  # Телевизоры
    print(
        category2.description)  # Современный телевизор, который позволяет наслаждаться просмотром, станет вашим
    # другом и помощником
    print(len(category2.products))  # 1
    print(category2.products)  # [...class Product object]

    print(Category.category_count)  # 2
    print(Category.product_count)  # 4

    raw_data = read_json_file(PATH)
    pprint(raw_data)

    categories_data = create_objects_from_json(raw_data)
    print(categories_data)

    print(categories_data[0].name)
    print(categories_data[0].products)
    print(categories_data[1].name)
    print(categories_data[1].products)
