import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from urllib.parse import urljoin

BASE_URL = 'https://maoyan.com'
user_agent ='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
Cookie='uuid_n_v=v1; uuid=6B59F970E50411EA96A68775497B19D8A0E3DEDA236D4F798D420555E83645BC; _csrf=36b6b16aee1f698593b96fb2d32951c0bdcbf0920ad0b2df2fe6898f2f10de2b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598161779; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=17419dd79a3c8-07cf98811062a3-3b634404-240000-17419dd79a346; _lxsdk=6B59F970E50411EA96A68775497B19D8A0E3DEDA236D4F798D420555E83645BC; mojo-uuid=178ad09e1a17d6be5f6610f3d8daf008; mojo-session-id={"id":"1a19dbcf17e920ed72c616199dd6b983","time":1598176965920}; mojo-trace-id=14; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598180506; __mta=245741243.1598161780166.1598176969750.1598180505706.5; _lxsdk_s=1741aef08a9-da7-54b-8d4%7C%7C12'
Cookie='__mta=245741243.1598161780166.1598179855606.1598181123354.7; uuid_n_v=v1; uuid=6B59F970E50411EA96A68775497B19D8A0E3DEDA236D4F798D420555E83645BC; _csrf=36b6b16aee1f698593b96fb2d32951c0bdcbf0920ad0b2df2fe6898f2f10de2b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598161779; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=17419dd79a3c8-07cf98811062a3-3b634404-240000-17419dd79a346; _lxsdk=6B59F970E50411EA96A68775497B19D8A0E3DEDA236D4F798D420555E83645BC; mojo-uuid=178ad09e1a17d6be5f6610f3d8daf008; mojo-session-id={"id":"1a19dbcf17e920ed72c616199dd6b983","time":1598176965920}; mojo-trace-id=31; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598181374; __mta=245741243.1598161780166.1598181123354.1598181373734.8; _lxsdk_s=1741aef08a9-da7-54b-8d4%7C%7C40'
Refer='https://maoyan.com/cinemas'
Cookie='BDUSS_BFESS=R6VzNCVENEdWhuRktKQmM5amx6ODlEc2pkVENpcEFXSUFFaVc4cnNWY3B3QzVmSVFBQUFBJCQAAAAAAAAAAAEAAAAlkvIOemRqMzIwOTI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACkzB18pMwdfNT; HMACCOUNT_BFESS=44FFB6C5A8A6B5BE'
Refer='https://www.baidu.com'
header ={'user-agent':user_agent,
         'Refer':Refer,
            'Cookie':Cookie}
         # 'Referer': 'https://maoyan.com/films'}

#获得前10个电影链接列表
def  get_url_list(url):
    response =requests.get(url,header)
    response.encoding='utf-8'
    bs_info=bs(response.text,'html.parser')
    print(response.text)
    urls=[]
   # for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}, limit=10):
    for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
        print(tags)
        for atag in tags.find_all('a'):
            #urls.apppend(f'https://maoyan.com'+ atag.get('bref'))
            single_url=urljoin(BASE_URL, atag.get('bref'))
            urls.append(single_url)
    return  urls


def get_moviesinfo(urls):
    mylist=[]
    header['Refer']='https://maoyan.com/board'
    for url in urls:
        response = requests.get(urls, header)
        bs_info = bs(response.text, 'html.parser')
        movie_name =bs_info.find('h1',attrs={'class':'name'}).text

        movie_type=''
        for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
            for atag in tags.find_all('a'):
                movie_type += atag

        #movie_release_time=bs_info.find('li',attrs={'class':'ellipsis'})[2]
        movie_release_time = bs_info.find('div', attrs={'class': 'movie-brief-container'}).find_all('li')[-1].text[:10]
        info_list=[movie_name,movie_type,movie_release_time]
        mylist.append(info_list)
        sleep(5)

    return mylist


def save(list):
    data=pd.DataFrame(list)
    #data.to_csv('./movie.csv',encoding='utf8',index=False,header=False)
    data.to_csv('./movie.csv',encoding='gbk',index=False,header=False)
    logging.info('save dato to csv')

def main(url):
    urls=get_url_list(url)
    movie_info_lists=get_moviesinfo(urls)
    save(movie_info_lists)

if __name__ == "__main__":
    url = 'https://maoyan.com/board/4'
    main(url)


