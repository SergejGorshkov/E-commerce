class Product:
    """Класс для создания товаров"""

    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество товара в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
