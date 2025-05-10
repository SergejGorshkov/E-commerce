from src.base_order import BaseOrder
from src.product import Product
from src.exceptions import ZeroQuantityProduct


class Order(BaseOrder):
    """Класс для описания заказа на купленный товар"""
    new_product: Product  # товар в заказе
    quantity: int  # количество товара в заказе

    @classmethod
    def add_product(cls, new_product, quantity) -> None:
        """Метод для получения информации о товаре в заказе (наименование, количество и итоговая стоимость)"""
        if new_product and issubclass(type(new_product), Product) and isinstance(quantity, int):
            if quantity <= 0:
                raise ZeroQuantityProduct("Нельзя добавить товар с нулевым или отрицательным количеством")
            else:
                print("Товар добавлен успешно")
                print(f'Товар в заказе: {new_product.name}, количество: {quantity}, итоговая стоимость: '
                      f'{new_product.price * quantity}.')
        else:
            raise TypeError("Попытка добавления несовместимого типа данных или пустого значения")
