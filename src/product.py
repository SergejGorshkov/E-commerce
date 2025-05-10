from src.base_product import BaseProduct
from src.print_mixin import PrintMixin
from src.exceptions import ZeroQuantityProduct


class Product(BaseProduct, PrintMixin):
    """Класс для создания товаров"""

    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество товара в наличии
    new_product: dict  # данные для добавления нового товара (ключи словаря соответствуют параметрам конструктора)
    new_price: float

    def __init__(self, name, description, price, quantity) -> None:
        """Конструктор для инициализации нового объекта класса Product"""

        self.name = name
        self.description = description
        self.__price = price
        if isinstance(quantity, int) and quantity > 0:
            self.quantity = quantity
        else:
            raise ZeroQuantityProduct("Товар с нулевым, дробным или отрицательным количеством не может быть добавлен")
        super().__init__()  # Вызов __init__ и __repr__ у миксина PrintMixin

    def __add__(self, other) -> float:
        """
        Метод для получения полной стоимости товаров класса Product
        (сумма произведений стоимости товаров на их количество)
        """
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError  # Вызов ошибки, если тип объекта не принадлежит классу Product

    def __str__(self) -> str:
        """Строковое представление экземпляра класса Product"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, new_product_dict, category_name):
        """Класс-метод, который принимает на вход параметры товара в виде словаря, извлекает значения,
        создает объект класса Product и возвращает его в случае, если товара еще нет в указанной категории.
        Если такой товар в категории уже есть, увеличивается его количество и изменяется цена, если цена переданного
        товара больше, чем текущая."""
        name = new_product_dict.get("name")
        description = new_product_dict.get("description")
        price = new_product_dict.get("price")
        quantity = new_product_dict.get("quantity")

        for product in category_name._products:  # Цикл перебора списка с описанием товаров из данной категории
            if name == product.name:  # Если название нового товара есть в списке с описанием текущего товара...
                product.quantity += quantity  # Количество текущего товара увеличивается на количество нового товара
                if price > product.price:  # Если цена нового товара больше цены имеющегося...
                    product.price = price  # цена имеющегося товара изменяется на большую
                print(f"При попытке добавления нового товара '{name}' в указанной категории обнаружен аналогичный "
                      f"товар. Количество товаров в указанной категории было увеличено. Новый товар не был добавлен.")
        else:
            return cls(name, description, price, quantity)  # Если товар новый, создается новый экземпляр класса
            # Product с переданными параметрами

    @property
    def price(self) -> float:
        """Геттер. Возвращает значение приватного атрибута - цена товара"""
        return self.__price

    @price.setter
    def price(self, new_price) -> float | None:
        """
        Сеттер. Изменяет значение приватного атрибута - цена товара.
        Если новая цена больше текущей, меняется на новую.
        Если меньше текущей, запрашивается подтверждение пользователя.
        Если <= 0, цена не меняется.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        elif new_price >= self.__price:
            self.__price = new_price
        else:
            answer = input(
                "Новая цена меньше текущей. Если подтверждаете снижение цены, введите 'y'. "
                "Для отмены введите 'n': ").lower().strip()
            if answer == "y":
                self.__price = new_price
            else:
                print("Снижение цены отменено")
