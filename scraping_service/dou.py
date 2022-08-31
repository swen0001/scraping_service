import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}


def dou(url):
    jobs = []
    errors = []
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='vacancyListId')
        if main_div:
            li_lst = main_div.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_lst:
                title = li.find('div', attrs={'class': 'title'})
                href = title.a['href']
                cont = li.find('div', attrs={'class': 'sh-info'})
                content = cont.text
                company = 'No name'
                a = title.find('a', attrs={'class': 'company'})
                if a:
                    company = a.text
                jobs.append({'title': title.text,
                             'url': href,
                             'description': content,
                             'company': company})
        else:
            errors.append({'url': url, 'title': "Div doesn`t exists"})
    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors

if __name__ == '__main__':
    url = 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D1%97%D0%B2&category=Python'
    jobs, errors = dou(url)
    h = codecs.open('dou.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()