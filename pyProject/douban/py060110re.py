import re
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}


def download_page(url):
    response = requests.get(url, headers=headers)
    html = response.text
    # print(html)

    home_page = BeautifulSoup(html, 'lxml')

    div = home_page.find('div', attrs={'class': 'paginator'})
    if div:
        page_obj_list = div.find_all('a')
        # print(page_obj_list)

        page_list = set()
        for page in page_obj_list:
            page_list.add(page.attrs.get('href'))
        # print(page_list)

        list_pa = [home_page]
        for url in page_list:
            print(f'下载分页{url}')
            page_obj = requests.get(url, headers=headers)
            page_o = BeautifulSoup(page_obj.text, 'lxml')
            list_pa.append(page_o)
        # print(list_pa)
    return list_pa


def ppp(list_pa):
    for lp in list_pa:
        reply_doc = lp.find_all('div', attrs={'class': 'reply-doc'})

        for rd in reply_doc:
            reply_content = rd.find('p', attrs={'class': "reply-content"})
            mail = re.search(r'\w+@\w+.\w+', reply_content.text, re.A)
            if mail:
                pubtime = rd.find('span', attrs={'class': "pubtime"})
                print(mail.group(), '\t\t\t', pubtime.text)


url = "https://www.douban.com/group/topic/198233257/"
list_pa = download_page(url)
ppp(list_pa)
