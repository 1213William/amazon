# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

"""
首先需要将所有的页数都找到，然后对url来进行循环，将里面想要的内容读取出来
"""
"""
1、首先需要对一页中的URL进行请求
2、根据某一页中的URL进行请求
3、解析这一页拿到所有我要的数据

"""


class SpSpider(scrapy.Spider):
    name = 'sp'
    allowed_domains = ['www.amazon.cn']
    start_urls = [
        'https://www.amazon.cn/s?k=女装',
        # 'https://www.amazon.cn/s?k=NBA',
        # 'https://www.amazon.cn/s?k=锅',
        # 'https://www.amazon.cn/s?k=碗',
        # 'https://www.amazon.cn/s?k=瓢',
        # 'https://www.amazon.cn/s?k=盆',
        # 'https://www.amazon.cn/s?k=男装',
    ]

    def start_requests(self):
        for i in self.start_urls:
            yield scrapy.Request(i, callback=self.get_all_url)

    def get_all_url(self, response):
        for i in range(1, 10 + 1):
            url = response.url + '&page=%s' % i
            yield scrapy.Request(url, callback=self.parse)

    # 对于这个parse我已经可以得到单个网页上的所有数据
    def parse(self, response):
        sel = Selector(response)
        container = []
        for i in sel.xpath(
                '//div[@class="s-result-list s-search-results sg-row"]'
                '/*[@class="sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item'
                ' sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"]'):
            title = i.xpath('div/span/div/div/div[2]/div[3]/div/div[1]/h2/a/span/text()').extract_first()
            low_price = i.xpath(
                'div/span/div/div/div[2]/div[4]/div/div/div/div/a/span/span[1]/span[1]/text()').extract_first()
            if not low_price:
                low_price = i.xpath(
                    'div/span/div/div/div[2]/div[4]/div/div/div/div/a/span/span[1]/text()').extract_first()
            high_price = i.xpath(
                'div/span/div/div/div[2]/div[4]/div/div/div/div/a/span/span[3]/span[1]/text()').extract_first()
            if not high_price:
                high_price = ''
            comments = i.xpath('div/span/div/div/div[2]/div[3]/div/div[2]/div/span[2]/a/span/text()').extract_first()
            if not comments:
                comments = ''
            print(title, low_price, high_price, comments)


# //*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[10]/div/span/div/div/div[2]/div[3]/div/div[2]/div/span[2]/a/span
# //*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[10]/div/span/div/div/div[2]/div[3]/div/div[2]/div/span[2]/a/span
# //*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/span/div/div/div[2]/div[4]/div/div[1]/div/div/a/span/span[3]/span[1]
#     container.append(i)
# print(len(container))
# //*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[4]/div/span/div/div/div[2]/div[4]/div/div[1]/div[1]/div/a/span/span[1]
# def parse(self, response):
#     sel = Selector(response)
#     # print(response.text)
#     page = sel.xpath('//li[@class="a-disabled"][2]/text()').extract_first()
#     if page:
#         for i in range(1, int(page) + 1):
#             url = response.url + '&page=%s' % str(i)
#
#             yield scrapy.Request(url, callback=self.parse_url)
#     else:
#         print('error')

# def parse_url(self, response):
#     sel = Selector(response)
#     # 这个时候的url是一个网页的url，所以就要根据这个url来进行解析
#     for li in sel.xpath(
#             '//div[@class="s-result-list s-search-results sg-row"]'):
#         # print(li.extract())
#         title = li.xpath('div/div/span/div/div/div[2]/div[3]/div/div[1]/h2/a/span/text()').extract_first()
#         low_price = li.xpath(
#             'div/div/span/div/div/div[2]/div[4]/div/div/div/div/a/span/span[1]/span[2]/span[2]/text()').extract_first()
#         # low_price = li.xpath('//span[@class="a-price-whole"]/text()').extract_first()
#         # if not low_price:
#         #     low_price = '0'
#         # print(low_price)
#         # //*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/span/div/div/div[2]/div[3]/div/div[1]/h2/a/span
#         print(title, low_price)
# title = sel.xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').extract_first()
# print(title)
