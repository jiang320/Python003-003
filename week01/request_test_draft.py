
from  lxml import html,etree


import  requests

from bs4 import BeautifulSoup

#file='D:\python_project\pythontrain_crawl\豆瓣电影 Top 250.html'
file='D:\python_project\pythontrain_crawl\TOP100榜 - 猫眼电影 - 一网打尽好电影.html'

file='D:\python_project\pythontrain_crawl\活着_购票_剧情介绍_演职人员_图集_猫眼电影.html'
#file='D:\python_project\pythontrain_crawl\影院热映大片_热映电影票房_高清电影影视大全-猫眼电影.html'

#tree=html.parse(file)

htmlfile=open(file,'r',encoding='utf-8')

bs_info=BeautifulSoup(htmlfile,features='lxml')

movie_brief = bs_info.find('div', attrs={'class': 'movie-brief-container'}).find_all('li')
print(movie_brief[-1].text[:10] )
#for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
#for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}):
for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
#for tags in bs_info.find_all('div', attrs={'class': 'ename ellipsis'}):
    for atag in tags.find_all('a'):
        print(atag.text)
    #     #for atag in tags.find_all('a'):
    #         print(atag.find('a').text)
        # # 获取所有链接
        # print(atag.get('href'))
        # # 获取电影名字
        # print(atag.get('title'))
        # # 获取电影发行时间
        # print(atag.get('releasetime'))



# for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
#     for atag in tags.find_all('a'):
#         # 获取所有链接
#         print(atag.get('href'))
#         # 获取电影名字
#         print(atag.find('span').text)





