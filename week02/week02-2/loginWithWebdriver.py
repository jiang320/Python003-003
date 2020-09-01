

from selenium import webdriver


import time


def scrape_shimo():
    browser=webdriver.Chrome()

    try:
        browser.get('https://shimo.im/login?from=home')
        time.sleep(2)
        browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('test')
        browser.find_element_by_xpath('//input[@name="password"]').send_keys('test')
        browser.find_element_by_xpath('//button[text()="立即登录"]').click()
    except Exception as e:
        print(e)
    finally:
        browser.close()