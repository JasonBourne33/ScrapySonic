import scrapy
from scrapy import Selector

from local_sonic.items import LocalSonicItem1


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html',
                       'https://sinoicglass.manufacturer.globalsources.com']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):

        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')

        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)

        body = '../localhtml/glass bong - Jining Sinoic Glass Products Co., Ltd..html'
        selector = Selector(text=open(body, encoding='gb18030', errors='ignore').read())
        # 这里获得所有a标签中的链接
        a_list = selector.xpath('//div[@class="product-lsit-box"]/div/ul/li/a')
        # 之后可以随意的调戏这个网页了(滑稽脸)
        for a in range(len(a_list)):
            pos = a
            img = a_list[a].xpath('./div[@class="mod-prod-img"]/img/@src').extract_first()
            title = a_list[a].xpath('./div[@class="mod-prod-info"]/div[@class="tit"]/span/text()').extract_first()
            href = a_list[a].xpath('./@href').extract_first()
            print("=======================")
            print(img)
            # print(title)
            # print(href)

            movie1 = LocalSonicItem1(pos=pos, title=title, img=img, href=href)
            yield movie1
            # yield  scrapy.Request(url=href,callback=self.parse_second,meta={'name':img})

    def parse_second(self, response):
        # 注意 如果拿不到数据的情况下  一定检查你的xpath语法是否正确
        src = response.xpath(
            '//div[@id="Product" and @class="descriptions"]//table/tbody/tr[1]/td[@class="ant-descriptions-item-content"]/text()').extract_first()
        # 接受到请求的那个meta参数的值
        name = response.meta['name']
        print("==============++++++++++++++++")
        print(src)
        movie = LocalSonicItem(src=src, name=name)

        yield movie
