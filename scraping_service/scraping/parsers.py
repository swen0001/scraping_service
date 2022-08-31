import requests
from bs4 import BeautifulSoup as BS
from random import randint


__all__ = ('work', 'dou', 'djinni')

headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'},
           {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
            "Accept": "*/*"},
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
           {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            "Accept": "*/*"}]


def work(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 3)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_lst = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_lst:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title.text,
                                 'url': domain + href,
                                 'description': content,
                                 'company': company,
                                 'city_id': city,
                                 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div doesn`t exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors


def dou(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 3)])
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
                                 'company': company,
                                 'city_id': city,
                                 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div doesn`t exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors


def djinni(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://djinni.co'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 3)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_ul = soup.find('ul', attrs={'class': 'list-jobs'})
            if main_ul:
                li_lst = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
                for li in li_lst:
                    title_a = li.find('div', attrs={'class': 'list-jobs__title'})
                    href = title_a.a['href']
                    cont = li.find('div', attrs={'class': 'list-jobs__description'})
                    content = cont.text
                    company = 'No name'
                    comp_div = li.find('div', attrs={'class': 'list-jobs__details__info'})
                    comp = comp_div.a
                    if comp:
                        company = comp.text.replace(" ", "")
                    jobs.append({'title': title_a.text,
                                 'url': domain + href,
                                 'description': content,
                                 'company': company,
                                 'city_id': city,
                                 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div doesn`t exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors
