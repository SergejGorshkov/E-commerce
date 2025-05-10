import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.product_lawngrass import LawnGrass
from src.product_smartphone import Smartphone


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
def some_product_2():
    """Фикстура для товара"""
    return Product(
        name="Iphone 15",
        description="Телефон для подчеркивания статуса",
        price=100000.0,
        quantity=5,
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
def empty_category():
    """Фикстура для категории товаров, не имеющая товаров"""
    return Category(
        name="Телевизоры",
        description="Современный телевизор - ваш друг и помощник",
        products=[]
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


@pytest.fixture
def product_iterator(first_category):
    """Фикстура с готовым итератором для категории `first_category` (данные - из фикстуры first_category)"""
    return ProductIterator(first_category)


@pytest.fixture
def smartphone_1():
    """Фикстура для товара класса Smartphone"""
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_2():
    """Фикстура для товара класса Smartphone"""
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass_1():
    """Фикстура для товара класса LawnGrass"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2():
    """Фикстура для товара класса LawnGrass"""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
