# _*_ encoding: utf-8 _*_
__author__ = 'hanhongyi'
__date__ = '2018/5/31 下午2:39'

from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from urllib.parse import urljoin
import scrapy

from lj.items import LjItem


class ljSpider(CrawlSpider):
    name = 'lj'
    allowed_domains = ['cd.lianjia.com']
    start_urls = ["https://cd.lianjia.com/ershoufang/pg1"]

    def parse(self, response):
        res = Selector(response)
        houses = res.xpath(".//ul[@class='sellListContent']/li")
        for house in houses:
            item = LjItem()
            item['title'] = house.xpath(".//div[@class='title']/a/text()").extract()[0]
            item['name'] = house.xpath(".//div[@class='houseInfo']/a/text()").extract()[0]
            item['house_type'] = house.xpath(".//div[@class='houseInfo']/text()").extract()[0]
            item['positionInfo'] = house.xpath(".//div[@class='positionInfo']/a/text()").extract()[0]
            item['followInfo'] = house.xpath(".//div[@class='followInfo']/text()").extract()[0]
            item['subway'] = house.xpath(".//span[@class='subway']/text()").extract()
            if item['subway'] ==[]:
                item['subway'] = '无信息'
            item['taxfree'] = house.xpath(".//span[@class='taxfree']/text()").extract()
            if item['taxfree'] ==[]:
                item['taxfree'] = '无信息'
            item['haskey'] = house.xpath(".//span[@class='haskey']/text()").extract()
            if item['haskey'] ==[]:
                item['haskey'] = '无信息'
            item['totalPrice'] = house.xpath(".//div[@class='totalPrice']/span/text()").extract()[0]
            item['unitPrice'] = house.xpath(".//div[@class='unitPrice']/span/text()").extract()[0]
            print(item)
            yield item
        page = res.xpath("//div[@class='page-box house-lst-page-box']/@page-data").re("\d+")
        print(page)
        if len(page)>1 and page[0] != page[1]:
            next_page = urljoin("https://cd.lianjia.com/ershoufang/pg1", "pg%s" % str(int(page[1]) + 1))
            yield scrapy.Request(next_page, callback=self.parse)
