import scrapy
from studyProject.zcool.zcool.items import ZcoolItem


class ZcSpider(scrapy.Spider):
    name = 'zc'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/']

    def parse(self, response):
        divList = response.xpath('//div[@class="work-list-box"]/div[@data-obj-id]')
        # print(len(divList))
        # print(divList)

        for div in divList:
            imgLink = div.xpath("./div[1]/a/img/@src").extract()[0]  # 1.封面图片链接
            # print(imgLink)
            title = div.xpath("./div[2]/p[1]/a/@title").extract_first()
            # print(title)
            types = div.xpath("./div[2]/p[2]/@title").extract()[0]
            # print(types)
            vistor = div.xpath("./div[2]/p[3]/span[1]/@title").extract_first()
            # print(vistor)
            comment = div.xpath("./div[2]/p[3]/span[2]/@title").extract()[0]
            # print(comment)
            likes = div.xpath("./div[2]/p[3]/span[3]/@title").extract_first()  # 6likes（推荐人数）
            # print(likes)
            item = ZcoolItem(imgLink=imgLink, title=title, types=types, vistor=vistor, comment=comment, likes=likes)
            yield item
            # print(item)
