import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}

url = 'https://rabota.ua/ua'
"""jobs = []
errors = []
domain = 'https://rabota.ua/ua/'"""
resp = requests.get(url, headers=headers)
"""if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    body = soup.find('div', attrs={'class': 'list-container'})"""
h = codecs.open('robota.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()