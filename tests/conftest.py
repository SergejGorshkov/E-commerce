import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def some_product():
    """Фикстура для товара"""
    return Product(
        name="Motorola",
        description="Телефон - легенда",
        price=1000.0,
        quantity=10,
    )


@pytest.fixture
def first_category():
    """Фикстура для первой категории товаров"""
    return Category(
        name="Смартфоны",
        description="Смартфоны - это весело и удобно!",
        products=[
            Product("Motorola", "Телефон - легенда", 1000.0, 10),
            Product("Samsung", "Телефон для повседневной жизни", 2000.0, 5)
        ]
    )


@pytest.fixture
def second_category():
    """Фикстура для второй категории товаров"""
    return Category(
        name="Телевизоры",
        description="Современный телевизор - ваш друг и помощник",
        products=[
            Product("Весна", "Старый добрый телевизор с кинескопом", 100.0, 2),
        ]
    )


@pytest.fixture
def mock_read_json_file():
    """Фикстура с тестовыми данными для чтения JSON-файла"""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны - это весело и удобно!",
            "products": [
                {
                    "name": "Motorola",
                    "description": "Телефон - легенда",
                    "price": 1000.0,
                    "quantity": 10
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор - ваш друг и помощник",
            "products": [
                {
                    "name": "Весна",
                    "description": "Старый добрый телевизор с кинескопом",
                    "price": 100.0,
                    "quantity": 2
                }
            ]
        }
    ]
