import json
import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class NcovSpider(object):
    def __init__(self):
        self.home_url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_html_by_url(self, url):
        response = requests.get(url)
        return response.content.decode()

    def parse_html(self, html, tag_id):
        soup = BeautifulSoup(html, 'lxml')
        script = soup.find(id=tag_id)
        text = script.string
        json_str = re.findall(r'\[.+\]', text)[0]
        data = json.loads(json_str)
        return data

    def save(self, data, path):
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl(self):
        home_page = self.get_html_by_url(self.home_url)

        last_day = self.parse_html(home_page, tag_id='getListByCountryTypeService2true')
        self.save(last_day, 'resrc/ncov053016.json')

    def crawl_virus(self):
        with open('resrc/ncov053016.json') as fp:
            js = json.load(fp)
        print(js)
        corona_virus = []
        for country in tqdm(js, '采集1月23号以来的各国疫情信息'):
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_html_by_url(statistics_data_url)
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']

            corona_virus.extend(statistics_data)
        self.save(corona_virus, 'resrc/ncov053017.json')

    def crawl_last_day_of_china(self):
        home_page = self.get_html_by_url(self.home_url)

        data = self.parse_html(home_page, tag_id='getAreaStat')

        self.save(data, 'resrc/ncov053018.json')

    def run(self):
        # self.crawl()
        # self.crawl_virus()
        self.crawl_last_day_of_china()


if __name__ == '__main__':
    spider = NcovSpider()
    spider.run()
