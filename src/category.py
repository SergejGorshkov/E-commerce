
class Category:
    """Класс для создания категорий товаров"""

    name: str             # название категории товаров
    description: str      # описание категории товаров
    products: list        # список товаров в данной категории (список объектов класса Product)
    category_count: int   # количество категорий товаров
    product_count: int    # количество товаров

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0  # Счетчик количества товаров будет увеличиваться
        # на длину списка товаров, если он существует. Если список пустой, тогда он не увеличивается
