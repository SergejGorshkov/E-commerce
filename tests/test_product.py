
def test_product_init(some_product):
    """Тест инициализации класса Product"""
    assert some_product.name == "Motorola"
    assert some_product.description == "Телефон - легенда"
    assert some_product.price == 1000.0
    assert some_product.quantity == 10
