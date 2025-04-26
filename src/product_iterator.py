from src.category import Category


class ProductIterator:
    """Класс для перебора товаров в категории"""
    category_object: Category  # Объект класса Category

    def __init__(self, category_object) -> None:
        """Конструктор для инициализации нового итератора класса ProductIterator"""
        self.category = category_object
        self.index = 0  # Переменная для перебора элементов последовательности (т.к. геттер `_products` из класса
        # Category - это список)
        # При создании объекта класса начальное значение индекса устанавливается на первый элемент последовательности

    def __iter__(self):
        """Метод для создания итератора с последовательностью объектов класса Product"""
        self.index = 0  # При каждом создании итератора индекс начинается с нуля (обнуляется)
        return self

    def __next__(self):
        """Метод для получения следующего элемента последовательности"""
        # Пока текущий индекс меньше длины списка товаров из геттера _products класса Category, выполняется перебор
        # списка и возврат очередного значения элемента последовательности
        if self.index < len(self.category._products):
            product = self.category._products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration  # При окончании перебора всего списка товаров нужно безопасно выйти из итератора
