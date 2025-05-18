from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс для создания подклассов"""

    @classmethod
    @abstractmethod
    def __add__(cls, other):
        """Метод для получения полной стоимости товаров класса Product
        (сумма произведений стоимости товаров на их количество)"""
        pass
