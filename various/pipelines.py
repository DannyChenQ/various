# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from twisted.enterprise import adbapi
import MySQLdb.cursors


class VariousPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='news',
                                            user='root', passwd='123123', cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8mb4', use_unicode=True)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute("select * from ifeng_news where link = %s",
                   (item['link'],))
        result = tx.fetchone()
        if result:
            logging.warning("Item already stored in db: %s" % item)
        else:
            tx.execute("insert into ifeng_news (title, news_time,link) "
                       "values (%s, %s,%s)",
                       (item['title'].encode("utf-8"),
                        item['news_time'],
                        item['link'])
                       )
            logging.info("Item stored in db: %s" % item, )

    def handle_error(self, e):
        logging.error(e)
