import json
import os

import requests
import telebot

from src.config import TOKEN, CHAT_ID, API_KEY, BASE, CURRENCY_RATES_FILE

bot = telebot.TeleBot(TOKEN)


def get_currency_rate(base: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float"""

    url = f"https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': {BASE}})
    rate = response.json()["rates"]["RUB"]
    return rate


def save_to_json(data: dict) -> None:
    """Сохраняет данные в json файл"""

    with open(CURRENCY_RATES_FILE, "a") as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump(data, f)
        else:
            with open(CURRENCY_RATES_FILE, "w") as json_file:
                json.dump(data, json_file)


def open_before_data(data: dict) -> None:
    '''Открываем существуюющий файл и возвращаем записанный курс'''

    with open(CURRENCY_RATES_FILE) as json_file:
        data_list = json.load(json_file)
        rate_before = data_list["rate"]
    return rate_before


def send_message_bot(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message,
    }
    response = requests.post(url, json=params)
    return response
