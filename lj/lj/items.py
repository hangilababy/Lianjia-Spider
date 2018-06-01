# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()
    house_type = scrapy.Field()
    positionInfo = scrapy.Field()
    followInfo = scrapy.Field()
    subway = scrapy.Field()
    taxfree = scrapy.Field()
    haskey = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()