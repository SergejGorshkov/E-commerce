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

if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым "
            "количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.get_middle_price())  # 140333.33

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.get_middle_price())  # 0
    order1 = Order.add_product(product1, 2)
