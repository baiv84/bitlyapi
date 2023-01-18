import sys
import json
import requests
from urllib.parse import urlparse

def get_token_value(fname='.env'):
    """Load token value from '.env' file"""
    try:
        with open(fname, 'r') as options:
            token = options.readline().split('=')[1]
            return token.lstrip().rstrip()
    except FileNotFoundError as e:
        print('Option file by default - .env NOT found. Abort!')
        sys.exit(1)
    return


def shorten_link(token, url):
    """Make link short via bitly service API"""
    print(token)
    
    headers = {
        'Authorization': 'Bearer %s' % (token),
        'Content-Type': 'application/json',
    }

    data = {
        'long_url': url,
        'domain': 'bit.ly',       
    }
    
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=json.dumps(data))
    if (response.ok == True):
        response_data = json.loads(response.text)
        bitlink = response_data['link']
        return bitlink
    else:
        raise requests.exceptions.HTTPError


def count_clicks(token, url):
    """Count clicks per link"""
    
    headers = {
        'Authorization': 'Bearer %s' % (token),
    }

    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )

    parsed = urlparse(url)
    bitlink_path = parsed.path.split('/')[1]
    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/bit.ly/%s/clicks' % (bitlink_path), headers=headers, params=params)
    data = json.loads(response.text)
    count_clicks = data['link_clicks'][0]['clicks']
    return count_clicks    
