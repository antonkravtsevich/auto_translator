import requests
from bs4 import BeautifulSoup
import random


def get_fresh_proxy():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.text)
    http_proxy = []
    https_proxy = []
    for tr in soup.find(id='proxylisttable').tbody.find_all('tr'):
        tds = tr.find_all('td')
        if tds[2] in ['UA', 'RU', 'PL']:
            ip = tds[0].text
            port = tds[1].text
            if tds[6].text == 'no':
                http_proxy.append('http://{}:{}'.format(ip, port))
            else:
                https_proxy.append('https://{}:{}'.format(ip, port))
    if not len(http_proxy) or not len(https_proxy):
        for tr in soup.find(id='proxylisttable').tbody.find_all('tr'):
            tds = tr.find_all('td')
            ip = tds[0].text
            port = tds[1].text
            if tds[6].text == 'no':
                http_proxy.append('http://{}:{}'.format(ip, port))
            else:
                https_proxy.append('https://{}:{}'.format(ip, port))

    return {
        'http': random.choice(http_proxy),
        'https': random.choice(https_proxy)
    }
        
