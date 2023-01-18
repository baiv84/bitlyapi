import re
from tools.url_shrinker import URLShrinker


CRYPTED_TOKEN = '98:53:48:50:97:49:98:49:55:50:50:98:97:55:49:48:101:49:48:56:49:52:51:53:53:54:99:49:53:98:55:56:98:99:48:98:55:56:101:55'
DECRYPTED_TOKEN = "".join([chr(int(c)) for c in CRYPTED_TOKEN.split(':')])


headers = {
    'Authorization': 'Bearer %s' % (DECRYPTED_TOKEN),
    'Content-Type': 'application/json',
}


data = '{ "long_url": "https://openwall.org/", "domain": "bit.ly" }'
response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
print(response.status_code)
print(response.text)
