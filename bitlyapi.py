import os
import json
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

#print(f"Hello, {name}. You are {age}.")

def is_bitlink(token, url):
    """Check link for bitlink type"""
    headers = {
        'Authorization': f'Bearer {token}',
    }

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    path = parsed_url.path.split('/')[1]

    api = f'https://api-ssl.bitly.com/v4/bitlinks/{hostname}/{path}/'
    response = requests.get(api, headers=headers)
    response.raise_for_status()

    print(response.text)
    return True

    
def shorten_link(token, url):
    """Make link short via bitly service API"""
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    data = {
        'long_url': url,
    }

    api = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(api, headers=headers, data=json.dumps(data))
    response.raise_for_status()

    return response.json()['link']
    

def count_clicks(token, url):
    """Count clicks per link"""
    headers = {
        'Authorization': f'Bearer {token}',
    }

    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )

    parsed = urlparse(url)
    bitlink = parsed.path.split('/')[1]
    api = f'https://api-ssl.bitly.com/v4/bitlinks/bit.ly/{bitlink}/clicks'
    response = requests.get(api, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    count_clicks = data['link_clicks'][0]['clicks']
    return count_clicks
    

if __name__ == '__main__':
    is_bitlink('', 'https://bit.ly/3XCCSZJ')

    # load_dotenv()
    # bitly_token = os.environ['BITLY_TOKEN']
    # user_input = input('Введите ссылку: ')

    # if is_bitlink(user_input):
    #     clicks = count_clicks(bitly_token, user_input)
    #     print(f'По вашей ссылке прошли: {clicks} раз(а)')
    # else:
    #     bitlink = shorten_link(bitly_token, user_input)
    #     print(bitlink)
