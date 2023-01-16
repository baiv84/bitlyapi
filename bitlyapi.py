import requests

headers = {
    'Authorization': 'Bearer b502a1b1722ba710e108143556c15b78bc0b78e7',
    'Content-Type': 'application/json',
}

data = '{ "long_url": "https://openbsd.org/", "domain": "bit.ly" }'



response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
print(response.status_code)
print(response.text)