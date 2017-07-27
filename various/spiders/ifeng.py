# -*- coding: utf-8 -*-
import scrapy
from various.items import IfengItem
import time


class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    allowed_domains = ['ifeng.com']
    start_urls = ['http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml']

    def parse(self, response):
        data = response.xpath("//div[@class='main']/div/div[@class='newsList']/ul")
        item = IfengItem()
        url_list = []
        for d in data:
            for ss in d.xpath(".//li"):
                item['title'] = ss.xpath(".//a/text()").extract()[0]
                item['news_time'] = ss.xpath(".//h4/text()").extract()[0]
                item['link'] = ss.xpath(".//a/@href").extract()[0]
                url_list.append(ss.xpath(".//a/@href").extract()[0])
                yield item
        for url in url_list:
            if url: yield scrapy.Request(url, callback=self.parse_item)
    def parse_item(self, response):
        print response
