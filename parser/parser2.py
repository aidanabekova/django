import requests
from bs4 import BeautifulSoup

from django.views.decorators.csrf import csrf_exempt

HOST = "https://zetfix.zone"
URL = "https://zetflix.zone/serials/legacies"

HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

}

@csrf_exempt
def get_html(url, params=''):
    r = requests.get(url, headers=HEADER, params=params)
    return r

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='custom-box')
    zetflix = []

    for item in items:
        zetflix.append(
            {
                'title': item.find('div', class_='sliderElement-t').get_text(strip=True),
                'image': HOST + item.find('div', class_='slider-poster').find('img').get('src')
            }
        )
    print(zetflix)
    return zetflix

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        zetflix = []
        for page in range(0, 3):
            html = get_html(URL, params={'page': page})
            zetflix.extend(get_data(html.text))
            return zetflix
    else:
        raise ValueError('Error in zetflix parser')



