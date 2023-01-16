import re
from tools.url_shrinker import URLShrinker


if __name__ == '__main__':
    url = input('Введите ссылку: ')
    shrinker = URLShrinker()    

    if (shrinker.http_available(url)):
        if (re.match('https://bit.ly/[A_Za-z0-9]+', url)):
            print('Bitly link MATCH')
        else:
            short_link = shrinker.shrink_url(url)
            print('Битлинк - %s' % short_link)
