import json

from src.category import Category
from src.product import Product


def read_json_file(path_to_file: str) -> list[dict]:
    """
    Функция чтения JSON-файла.
    Принимает абсолютный путь к JSON-файлу для извлечения данных.
    Возвращает список словарей с данными.
    """
    data_json = []  # По умолчанию данные отсутствуют
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            data_json = json.load(file)
    except json.JSONDecodeError:
        print("Ошибка декодирования файла.")
    except FileNotFoundError:
        print(f"Ошибка! Файл по адресу {path_to_file} не найден.")

    if not isinstance(data_json, list):
        return []

    return data_json  # Возврат содержимого JSON-файла или пустого списка в случае, если файл пустой, содержит
    # не-список или не найден


def create_objects_from_json(data: list[dict]) -> list:
    """
    Функция создания объектов класса.
    Принимает список словарей.
    Возвращает список с объектами классов.
    """
    categories = []
    for category in data:
        products = []
        for product in category.get("products"):
            products.append(Product(**product))  # Распаковка словарей с товарами под ключом `products`
            # из файла `products.json`
        category["products"] = products  # Теперь вместо списка словарей по ключу `products` будет находиться список
        # экземпляров класса Product
        categories.append(Category(**category))  # Распаковка словарей с категориями товаров из файла `products.json`

    return categories
