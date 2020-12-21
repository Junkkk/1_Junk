import requests

from bs4 import BeautifulSoup
from requests.models import Response
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from pprint import pprint


URL = 'https://www.python.org'


def get_month():
    curr_month = datetime.now().month
    next_month = datetime.now() + relativedelta(month=1)
    return curr_month, next_month.month


def get_html(url: str) -> Response:
    return requests.get(url)


def get_content(html: str) -> list:
    content = []
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='medium-widget event-widget last').find_all('li')
    for item in items:
        data = {
            'name': item.find('a').get_text(strip=True),
            'date': item.find('time').get('datetime'),
            'url': item.find('a').get('href')
        }
        content.append(data)
    return content


def parse_content(content: list) -> dict:
    curr_month, next_month = get_month()
    out_data = {
        'current_month': [],
        'next_month': []
    }
    for content_data in content:
        content_data['url'] = URL + content_data['url']
        date = parse(content_data['date'])
        if date.month == curr_month:
            out_data['current_month'].append(content_data)
        elif date.month == next_month:
            out_data['next_month'].append(content_data)
    return out_data


def parse_html():
    html = get_html(URL)
    if html.status_code == 200:
        content = get_content(html.text)
        pprint(parse_content(content))
    else:
        print('Error')


if __name__ == '__main__':
    parse_html()
