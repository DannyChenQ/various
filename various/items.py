# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IfengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    news_time = scrapy.Field()
    content  = scrapy.Field()
    link = scrapy.Field()
    catch_time = scrapy.Field()
    # pass
