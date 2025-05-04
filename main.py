import os

from src.category import Category
# from src.product_iterator import ProductIterator
# from src.product_smartphone import Smartphone
from src.order import Order
# from src.product_lawngrass import LawnGrass
from src.product import Product

# from pprint import pprint

# from src.utils import create_objects_from_json, read_json_file

PATH = os.path.join(os.path.dirname(__file__), "data", "products.json")  # Путь к JSON-файлу

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    print()
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для"
                         " удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")  # True
    print(category1.description)  # Смартфоны, как средство не только коммуникации, но и получения дополнительных
    # функций для удобства жизни
    print(len(category1.products))  # 3
    print(category1.category_count)  # 1
    print(category1.product_count)  # 3

    print()
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом "
                         "и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))  # 1
    print(category2.products)  # ['55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n']

    print(Category.category_count)  # 2
    print(Category.product_count)  # 4

    print()
    print(Order.add_product(product1, 2))  # Товар в заказе: Samsung Galaxy S23 Ultra, количество: 2,
    # итоговая стоимость: 360000.0.
