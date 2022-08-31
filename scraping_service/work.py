import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}


def work(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers)
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
                             'company': company})
        else:
            errors.append({'url': url, 'title': "Div doesn`t exists"})
    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors

"""
def robota(url):
    jobs = []
    errors = []
    domain = 'https://rabota.ua/ua/'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        body = soup.find('div', attrs={'class': 'list-container'})
        h = codecs.open('work.txt', 'w', 'utf-8')
        h.write(str(body))
        h.close()
        
        if body:
            print('ok')
            body_lst = body.find_all('div', attrs={'class': 'ng-star-inserted'})
            for div in body_lst:
                title = div.find('h2')
                href = div.find('a').a['href']
                content = 'More info'
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'title': title.text,
                             'url': domain + href,
                             'description': content,
                             'company': company})
        else:
            errors.append({'url': url, 'title': "Body doesn`t exists"})
    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors

"""
if __name__ == '__main__':
    url = 'https://rabota.ua/ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'
    jobs, errors = robota(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
