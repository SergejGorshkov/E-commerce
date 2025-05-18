class ZeroQuantityProduct(Exception):
    """Класс-исключение, который обрабатывает случай добавления товара с нулевым значением количества товаров
        и выводит пользователю соответствующее сообщение"""
    def __init__(self, message=None):
        super().__init__(message)
