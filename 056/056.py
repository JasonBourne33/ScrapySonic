

from scrapy import Selector

#前路径，主div   //div[@class="product-lsit-box"]/div/ul/li/a/
#第一页图片      //div[@class="product-lsit-box"]/div/ul/li/a/div[@class="mod-prod-img"]/img/@src
#第一页标题      //div[@class="product-lsit-box"]/div/ul/li/a/div[@class="mod-prod-info"]/div[@class="tit"]/span/text()
#第二页的链接    //div[@class="product-lsit-box"]/div/ul/li/a/@href
#第二页的产品编号 //div[@id="Product" and @class="descriptions"]//table/tbody/tr[1]/td[@class="ant-descriptions-item-content"]/text()


body = './localhtml/ glass bong - Jining Sinoic Glass Products Co., Ltd..html'
# body = open('离线网页保存地址/test.html').read()
#使用scrapy自身的Selector解析文本
selector = Selector(text=open(body, encoding='gb18030', errors='ignore').read())

#这里获得所有a标签中的链接
a_list = selector.xpath('//div[@class="product-lsit-box"]/div/ul/li/a')
#之后可以随意的调戏这个网页了(滑稽脸)
for a in a_list:
    img = a.xpath('./div[@class="mod-prod-img"]/img/@src').extract_first()
    title = a.xpath('./div[@class="mod-prod-info"]/div[@class="tit"]/span/text()').extract_first()
    href = a.xpath('./@href').extract_first()
    print("=======================")
    print(img)
    print(title)
    print(href)

    # yield  scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})


# print(a_list)

