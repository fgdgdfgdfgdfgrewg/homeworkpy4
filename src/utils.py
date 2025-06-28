import logging
import os
from typing import Tuple

# Создание папки для логов
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Настройка логгера для модуля utils
logger_utils: logging.Logger = logging.getLogger("utils")
logger_utils.setLevel(logging.DEBUG)

# Обработчик файла
file_handler_utils: logging.FileHandler = logging.FileHandler(
    filename=os.path.join(LOG_DIR, "utils.log"),
    mode="w",
    encoding="utf-8"
)
file_handler_utils.setLevel(logging.DEBUG)

# Форматировщик
file_formatter_utils: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler_utils.setFormatter(file_formatter_utils)

# Добавление обработчика
logger_utils.addHandler(file_handler_utils)


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 4 и последние 4 цифры"""
    try:
        masked = f"{card_number[:4]} **** **** {card_number[-4:]}"
        logger_utils.info(f"Карта успешно замаскирована: {card_number}")
        return masked
    except Exception as e:
        error_msg = f"Ошибка маскировки карты: {e}"
        logger_utils.error(error_msg, exc_info=True)
        raise


def get_account_info(account: str) -> Tuple[str, str]:
    """Возвращает тип счета и последние 4 цифры"""
    try:
        account_type = "Счет" if "счет" in account.lower() else "Карта"
        last_digits = account[-4:]
        logger_utils.info(f"Информация о счете получена: {account}")
        return account_type, last_digits
    except Exception as e:
        error_msg = f"Ошибка получения информации о счете: {e}"
        logger_utils.error(error_msg, exc_info=True)
        raise
