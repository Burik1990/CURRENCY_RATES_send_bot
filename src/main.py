from datetime import datetime
from dotenv import load_dotenv

from src.config import BASE
from utils import send_message_bot, get_currency_rate, open_before_data, save_to_json

load_dotenv()


def main():
    """
    Основная функция программы.
    получает текущий курс валюты USD от API. Записывает данные в json файл.
    Провяряем И если курс меняется отправляем сообщение в телегу
    """

    rate = get_currency_rate(BASE)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"currency": BASE, "rate": rate, "timestamp": timestamp}

    if open_before_data(data) != rate:
        result = f"Курс изменился: {BASE} к рублю был - {open_before_data(data)}, стал - {rate}"
        send_message_bot(result)
        save_to_json(data)


if __name__ == '__main__':
    main()
