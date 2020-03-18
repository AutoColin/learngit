# -*- coding: utf-8 -*-
import scrapy
import re

class StockinfoSpider(scrapy.Spider):
    name = 'stockinfo'
    start_urls = ['https://quote.stockstar.com/stock/stock_index.htm']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]_\d{6}', href)[0][-6:]
                url = 'http://quote.cfi.cn/' + stock + '.html'
                yield scrapy.Request(url, callback = self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}

        name = response.css('.Lfont::text').extract()[0]
        value = response.css('#last::text').extract()[0]

        infoDict.update({name : value})

        yield infoDict
