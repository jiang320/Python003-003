# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from  work2_maoyanSpider.items import Work2MaoyanspiderItem

BASE_URL = 'https://maoyan.com'
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films']

    def start_requests(self):
        yield scrapy.Request(url=f'https://mapyan.com/films',callback=self.parse())

    def parse(self, response):
        #/html/body/div[4]/div/div[2]/div[2]/dl/dd[1]/div[2]
        ##app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(1) > div.channel-detail.movie-item-title
        tags=Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')[:10]
        for tag in tags:
            url=BASE_URL+tag.xpath('./a/@hbref').extract_first()
            yield scrapy.Request(url=url,callback=self.parse2)

    def parse2(self,response):


        item=Work2MaoyanspiderItem()

#/html/body/div[3]/div/div[2]/div[1]
        #body > div.banner > div > div.celeInfo-right.clearfix > div.movie-brief-container
        movie_brief=Selector(response=response).xpath('//div[@class="movie-brief-container"]')
#/html/body/div[3]/div/div[2]/div[1]/h1
        name=movie_brief.xpath('./h1/text()').extract()
#/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]
        categories=movie_brief.xpath('./ul/li/a').extract()
#/html/body/div[3]/div/div[2]/div[1]/ul/li[3]
        published_at=movie_brief.xpath('./ul/li[last()]/text()').extract()

        item['name']=name
        item['categories']=[category.strip()  for category in categories]
        item['published-at'] =published_at


        yield item



