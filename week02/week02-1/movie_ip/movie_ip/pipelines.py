# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MovieIpPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='192.168.88.170', user='root', password='root')
        self.cursor = self.conn.cursor()
        pymysql.charset = 'gbk'
        # self.article = open('./doubanmovie.csv', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_actors = item['movie_actors']
        movie_release_time = item['movie_release_time']

        try:
            self.cur.execute(
                "insert into scrapy(movie_name, movie_type, movie_actors,movie_release_time,movie_release_time) values(%s,%s,%s)" % (movie_name, movie_type, movie_actors,movie_release_time,movie_release_time))
            self.conn.commit()
        except Exception as err:
            self.rollback()
            print(err)
            # output = f'|{movie_name}|\t|{movie_type}|\t|{movie_actors}|\n\n'
            # self.article.write(output)

        return item

        def close_spider(self, spider):
            self.conn.close()

