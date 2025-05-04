from src.base_order import BaseOrder
from src.product import Product


class Order(BaseOrder):
    """Класс для описания заказа на купленный товар"""
    product: Product  # товар в заказе
    quantity: int  # количество товара в заказе

    @classmethod
    def add_product(cls, product, quantity) -> str:
        """Метод для получения информации о товаре в заказе (наименование, количество и итоговая стоимость)"""

        if all((product, quantity)) and issubclass(type(product), Product) and quantity >= 0 and isinstance(quantity,
                                                                                                            int):
            return (f'Товар в заказе: {product.name}, количество: {quantity}, итоговая стоимость: '
                    f'{product.price * quantity}.')
        else:
            raise TypeError("Неверное значение переданного аргумента")
