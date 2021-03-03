# -*- coding: utf-8 -*-
import scrapy


class LivecoinSpider(scrapy.Spider):
    name = 'livecoin'
    allowed_domains = ['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/']
    start_urls = ['http://https://web.archive.org/web/20200116052415/https://www.livecoin.net/en//']

    def parse(self, response):
        pass
