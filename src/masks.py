import logging
import os
from typing import Union

# Создание папки для логов
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Настройка логгера для модуля masks
logger_masks: logging.Logger = logging.getLogger("masks")
logger_masks.setLevel(logging.DEBUG)

# Обработчик файла
file_handler_masks: logging.FileHandler = logging.FileHandler(
    filename=os.path.join(LOG_DIR, "masks.log"),
    mode="w",
    encoding="utf-8"
)
file_handler_masks.setLevel(logging.DEBUG)

# Форматировщик
file_formatter_masks: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler_masks.setFormatter(file_formatter_masks)

# Добавление обработчика
logger_masks.addHandler(file_handler_masks)


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры"""
    try:
        masked = f"**{account_number[-4:]}"
        logger_masks.info(f"Счет успешно замаскирован: {account_number}")
        return masked
    except Exception as e:
        logger_masks.error(f"Ошибка маскировки счета: {e}", exc_info=True)
        raise


def process_payment(payment_data: dict) -> Union[str, None]:
    """Обрабатывает платежные данные"""
    try:
        # Логика обработки платежа
        logger_masks.info("Платеж успешно обработан")
        return "success"
    except Exception as e:
        logger_masks.error(f"Ошибка обработки платежа: {e}", exc_info=True)
        return None
