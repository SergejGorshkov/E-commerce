import json
from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, read_json_file


def test_read_json_file_successful(mock_read_json_file):
    """Тест успешного чтения файла с данными `products.json`"""
    # Мокаем JSON-файл и подменяем данные, "прочитанные" из JSON-файла
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_read_json_file))):
        # Вызываем тестируемую функцию
        result = read_json_file("some_path_to_file")

        # Проверяем результаты
        assert len(result) == 2
        assert isinstance(result, list)


def test_read_json_file_if_file_not_found():
    """Тест случая, когда JSON-файл с данными `products.json` не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("some_path_to_file")
        assert result == []


def test_read_json_file_if_invalid_json():
    """Тест случая с неправильным JSON"""
    with patch("builtins.open", mock_open(read_data="Ошибка декодирования файла.")):
        result = read_json_file("some_path_to_file")
        assert result == []


######################################################################################

def test_create_objects_from_json_successful(mock_read_json_file):
    result = create_objects_from_json(mock_read_json_file)
    assert len(result) == 2
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
