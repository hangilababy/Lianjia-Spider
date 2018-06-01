# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

from lj.settings import mysql_config


class LjPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(**mysql_config)

    def process_item(self, item, spider):
        with self.db.cursor() as cursor:
            sql = "insert into houses VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (item['title'],
                                 item['name'],
                                 item['house_type'],
                                 item['positionInfo'],
                                 item['followInfo'],
                                 item['subway'],
                                 item['taxfree'],
                                 item['haskey'],
                                 item['totalPrice'],
                                 item['unitPrice']
                                 ))
            self.db.commit()
        return item
