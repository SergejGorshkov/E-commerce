from src.product import Product


class LawnGrass(Product):
    """Подкласс класса Product для создания товара 'LawnGrass' (Трава газонная) """
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество товара в наличии
    country: str  # страна-производитель
    germination_period: str  # срок прорастания
    color: str  # цвет

    def __init__(self, name, description, price, quantity, country, germination_period, color) -> None:
        """Конструктор для инициализации нового объекта класса LawnGrass (дочернего класса от Product)"""
        super().__init__(name, description, price, quantity)  # Вызов __init__ у класса Product

        self.__price = price
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other) -> float:
        """
        Метод для получения полной стоимости товаров подкласса LawnGrass класса Product
        (сумма произведений стоимости товаров на их количество)
        """
        if type(other) is LawnGrass:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError("Попытка сложения товаров разных классов")
