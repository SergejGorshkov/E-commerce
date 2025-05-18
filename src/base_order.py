from abc import ABC, abstractmethod


class BaseOrder(ABC):
    """Базовый класс для создания подклассов"""

    @classmethod
    @abstractmethod
    def add_product(cls, *args, **kwargs):
        """Метод для добавления товара класса Product"""
        pass
