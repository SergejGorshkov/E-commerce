from src.category import Category


def test_category_init(first_category, second_category):
    """Тест инициализации класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны - это весело и удобно!"
    assert len(first_category.products) == 2

    assert len(second_category.products) == 1

    assert Category.category_count == 2  # Количество категорий
    assert Category.product_count == 3  # Количество товаров во всех категориях

    # Количество категорий для обоих пользователей должно быть одинаковым и равным сумме всех категорий
    assert first_category.category_count == 2
    assert second_category.category_count == 2
