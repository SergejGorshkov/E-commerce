from src.product import Product


class Smartphone(Product):
    """Подкласс класса Product для создания товара 'Smartphone' """
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество товара в наличии
    efficiency: float  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color) -> None:
        """Конструктор для инициализации нового объекта класса Smartphone (дочернего класса от Product)"""
        super().__init__(name, description, price, quantity)  # Вызов __init__ у класса Product

        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other) -> float:
        """
        Метод для получения полной стоимости товаров подкласса Smartphone класса Product
        (сумма произведений стоимости товаров на их количество)
        """
        if type(other) is Smartphone:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError("Попытка сложения товаров разных классов")
