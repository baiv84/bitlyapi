import os
import requests
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def get_arguments_parser():
    """Return argument parsing object"""
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument ('long_url', nargs='?')
    return argument_parser


def shorten_link(bitly_token, url):
    """Make shorten link via bitly service API"""
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {bitly_token}'}
    json = {'long_url': url}

    response = requests.post(api_url, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitly_token, url):
    """Count summary click statistic"""
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    path = parsed_url.path

    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{hostname}{path}/clicks/summary'
    headers = {'Authorization': f'Bearer {bitly_token}'}
    params = (('unit', 'month'),)
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitly_token, url):
    """Check link for bitlink type"""
    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    path = parsed_url.path

    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{hostname}{path}'
    headers = {'Authorization': f'Bearer {bitly_token}'}
    response = requests.get(api_url, headers=headers)
    return response.ok


if __name__ == '__main__':
    argument_parser = get_arguments_parser()
    namespace = argument_parser.parse_args()
    long_url = namespace.long_url

    if os.path.exists('.env'):
        load_dotenv()
        bitly_token = os.environ['BITLY_TOKEN']
        if long_url is not None:
            user_input = long_url
        else:
            user_input = input('Введите ссылку: ')
        
        bitly_flag = is_bitlink(bitly_token, user_input)
        if bitly_flag:
            try:
                clicks_number = count_clicks(bitly_token, user_input)
                print(f'По вашей ссылке прошли: {clicks_number} раз(а)')
            except requests.HTTPError:
                print('Операция подсчета ссылок - '
                      'Вы ввели неправильную ссылку ! - 1')
        else:
            try:
                bitlink = shorten_link(bitly_token, user_input)
                print(f'Битлинк: {bitlink}')
            except requests.HTTPError:
                print('Операция сжатия ссылки - '
                      'Вы ввели неправильную ссылку ! -2')
    else:
        print('\n*************************************************'
              '\nОтсутствует файл настроек - ".env"'
              '\nТокен не доступен'
              '\nДальнейшее выполнение программы не возможно !'
              '\n*************************************************\n')
