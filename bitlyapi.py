# -*- coding: utf-8 -*-

import os
import sys
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
from tools.bitly_apy_callers import shorten_link, count_clicks


def is_bitlink(url):
    """Check for bit.ly link"""
    parsed = urlparse(url)
    if (parsed.netloc == 'bit.ly'):
        return True
    return False


if __name__ == '__main__':
    # Load API token
    try:
        load_dotenv()
        token = os.environ['TOKEN']
    except KeyError:
        print('Ошибка обработки файла настроек (.env)!')
        sys.exit(1)

    if token is not None:
        while True:
            user_input = input('Введите ссылку (Для выхода введите exit): ')
            # Exit checks
            if user_input == 'exit':
                break
            # Bitlink -> start clicks counting
            if is_bitlink(user_input) is True:
                try:
                    clicks = count_clicks(token, user_input)
                    print('По вашей ссылке прошли: %s раз(а)' % (clicks))
                except requests.exceptions.HTTPError:
                    print('\n******************************************'
                          '\nОшибка в HTTP-запросе. '
                          '\nПроверьте корректность bit.ly ссылки !'
                          '\n******************************************')
            # Common link -> start link shorting
            else:
                try:
                    bitlink = shorten_link(token, user_input)
                    print(bitlink)
                except requests.exceptions.HTTPError:
                    print('\n******************************************\n'
                          '\nОшибка в HTTP-запросе.'
                          '\nURL-адрес должен включать префикс http (https)'
                          '\nв начале адресной строки !'
                          '\n\n******************************************')
                    continue
    else:
        print('Ошибка API-токена')
