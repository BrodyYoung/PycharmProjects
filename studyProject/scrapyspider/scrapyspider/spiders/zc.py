def parse(self, response):
    divList = response.xpath('//div[@class="work-list-box"]/div')
    print(len(divList))