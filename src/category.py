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

    def __init__(self, name, description, products=None):
        """Конструктор для инициализации нового объекта класса Category"""
        self.name = name
        self.description = description
        self.__products = products if products else []  # Приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products) if products else 0  # Счетчик количества товаров будет увеличиваться
        # на длину списка товаров, если он существует. Если список пустой, тогда он не увеличивается

    def add_product(self, new_product):
        """Метод для добавления в список товаров нового товара класса Product"""
        if new_product and isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1

    @property
    def products(self):
        """Геттер. Построчно выводит список товаров в виде строк"""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in
                self.__products]

    @property
    def _products(self):
        """Геттер. Выводит список товаров в категории в виде списка"""
        return [product for product in self.__products]
