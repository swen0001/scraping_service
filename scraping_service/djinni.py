import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}


def djinni(url):
    jobs = []
    errors = []
    domain = 'https://djinni.co'
    resp = requests.get(url, headers=headers)
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
                             'company': company})
        else:
            errors.append({'url': url, 'title': "Div doesn`t exists"})
    else:
        errors.append({'url': url, 'title': "Page do not response"})
    return jobs, errors


if __name__ == '__main__':
    url = 'https://djinni.co/jobs/keyword-python/kyiv/?region=UKR'
    jobs, errors = djinni(url)
    h = codecs.open('djinni.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
