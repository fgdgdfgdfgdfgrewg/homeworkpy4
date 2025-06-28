from src.masks import mask_account_number, process_payment
from src.utils import get_account_info, mask_card_number

if __name__ == "__main__":
    # Примеры вызова функций
    print(mask_card_number("1234567890123456"))
    print(mask_account_number("1234567890"))

    account_info = get_account_info("Счет 1234567890123456")
    print(account_info)

    payment_result = process_payment({"amount": 100, "currency": "RUB"})
    print(payment_result)
