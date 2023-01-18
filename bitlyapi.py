import sys
import requests
from tools.bitly_apy_callers import shorten_link, count_clicks, get_token_value
from urllib.parse import urlparse


def is_bitlink(url):
    """Check for bit.ly link"""
    parsed = urlparse(url)
    if (parsed.netloc == 'bit.ly'):
        return True
    return False

    

if __name__ == '__main__':
    # Retrieve API token from setting file
    token = get_token_value()

    if token is not None:
        while True:
            user_input = input('Enter link to short (Print "exit" to stop): ')
            if user_input == 'exit':
                break

            if is_bitlink(user_input) == True: 
                print('we have bitlink !')
                clicks = count_clicks(token, user_input)
                print(clicks)
                
            else:
                try:
                    bitlink = shorten_link(token, user_input)
                    print(bitlink)
                except requests.exceptions.HTTPError:
                    print('Exception occured. Abort program !')
                    sys.exit(1)
        
    else:
        print('Token error')
