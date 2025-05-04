from src.product import Product
from src.product_lawngrass import LawnGrass
from src.product_smartphone import Smartphone


def test_print_mixin(capsys):  # Перехват потока вывода в консоль при создании нового экземпляра класса Product
    Product(name="Motorola", description="Телефон - легенда", price=1000.0, quantity=10)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product("Motorola", "Телефон - легенда", 1000.0, 10)'

    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
               "S23 Ultra", 256, "Серый")
    message = capsys.readouterr()
    assert message.out.strip() == ('Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", '
                                   '180000.0, 5)')

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20)'
