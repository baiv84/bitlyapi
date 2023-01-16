import json
import requests


class URLShrinker(object):
    # Token access
    token = 'b502a1b1722ba710e108143556c15b78bc0b78e7'

    def __init__(self):
        """Initialize pure object"""
        super().__init__()


    def http_available(self, url):
        """Check site availability before shrink API call"""
        flag = False
        try:
            response = requests.get(url)
            if (response.status_code < 400):
                flag = True
            else:
                flag = False
        except:
            print('Ссылка - %s не доступна' % url)
        return flag
    

    def shrink_url(self, long_url):
        """Shrink long URL to short bitly link"""
        headers = {
            'Authorization': 'Bearer %s' % (URLShrinker.token),
            'Content-Type': 'application/json',
        }

        data = json.dumps({
            'long_url': long_url,
            'domain': 'bit.ly'
        })
        
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
        pure_resp = response.json()
        return pure_resp['link']

