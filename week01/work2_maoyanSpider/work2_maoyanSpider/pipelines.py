# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class Work2MaoyanspiderPipeline:
    def process_item(self, item, spider):
        name =item['name']
        categories = item['categories']
        published_at = item['published_at']

        movie=pd.DataFrame({
            'name':name,
            'categories':[categories],
            'published_at':published_at
        })
        movie.to_csv('./movie.csv',
                     mode='a',
                     encoding='utf8',
                     index=False,
                     header=False)

