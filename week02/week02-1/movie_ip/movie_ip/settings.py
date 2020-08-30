# -*- coding: utf-8 -*-

# Scrapy settings for movie_ip project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movie_ip'

SPIDER_MODULES = ['movie_ip.spiders']
NEWSPIDER_MODULE = 'movie_ip.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movie_ip (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

COOKIE = '216258089.1598800579935.1598800579935.1598800604716.2; uuid_n_v=v1; uuid=C18F8970EAD311EA94345B95E7867004112D0F8A15C1499783C5DA06D761805C; _csrf=cd1c92e32ee9b262c968e020d9c24e9de762aa981273ccf70a7c18a80b2c4121; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598800579; mojo-uuid=0bce3737c158477d9be3e2777256211f; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=1743ff0ccb4c8-01b8a92e19be8b-3b634404-144000-1743ff0ccb4c8; _lxsdk=C18F8970EAD311EA94345B95E7867004112D0F8A15C1499783C5DA06D761805C; mojo-session-id={"id":"115156680fe9537a2dbe2b280dff7ab4","time":1598800579774}; __mta=216258089.1598800579935.1598800579935.1598800579935.1; mojo-trace-id=3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598800605; _lxsdk_s=1743ff0ccb5-06-d93-df2%7C%7C4'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movie_ip.middlewares.MovieIpSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'movie_ip.middlewares.MovieIpDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'movie_ip.middlewares.RandomHttpProxyMiddleware': 300
}


HTTP_PROXY_LIST =[
    'http://52.179.231.206:80',
    'http://95.0.194.241:9090',
]


ITEM_PIPELINES = {
   'movie_ip.pipelines.MovieIpPipeline': 300,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'movie_ip.pipelines.MovieIpPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
