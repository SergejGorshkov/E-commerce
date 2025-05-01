from src.product import Product


class Category:
    """Класс для создания категорий товаров"""

    name: str  # название категории товаров
    description: str  # описание категории товаров
    products: list  # список товаров в данной категории (список объектов класса Product)
    category_count: int  # количество категорий товаров
    product_count: int  # количество товаров

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None) -> None:
        """Конструктор для инициализации нового объекта класса Category"""
        self.name = name
        self.description = description
        self.__products = products if products else []  # Приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products) if products else 0  # Счетчик количества товаров будет увеличиваться
        # на длину списка товаров, если он существует. Если список пустой, тогда он не увеличивается

    def __str__(self) -> str:
        """Строковое представление экземпляра класса Category"""
        sum_quantity = 0
        for product in self.__products:  # Перебор товаров в категории и суммирование их количества
            sum_quantity += product.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    def add_product(self, new_product) -> None:
        """Метод для добавления в список товаров нового товара класса Product"""
        if new_product and issubclass(type(new_product), Product):
            self.__products.append(new_product)
            Category.product_count += 1
            return
        raise TypeError

    @property
    def products(self) -> list[str]:
        """Геттер. Построчно выводит список товаров в виде строк"""
        return [f"{str(product)}\n" for product in self.__products]

    @property
    def _products(self) -> list[Product]:
        """Геттер. Выводит список товаров в категории в виде списка"""
        return [product for product in self.__products]
