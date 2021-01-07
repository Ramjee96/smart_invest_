from selenium import webdriver
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\ChromeWebDriver\\chromedriver.exe")

url = 'https://finance.naver.com/item/main.nhn?code=121800'
driver.get(url)

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

name = soup.select_one('#middle.new_totalinfo>div.h_company>div.wrap_company>h2>a').text
current_price = soup.select_one('#chart_area.spot>div.rate_info>div.today>p.no_today>em.no_up>span').text
Market_capital = soup.select_one('#_market_sum').text
Sales = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(1) > td:nth-child(4)').text
ROE = soup.select_one('#content > div.section.cop_analysis > div.sub_section > table > tbody > tr:nth-child(6) > td:nth-child(10)')

print(name, current_price, Market_capital, Sales, ROE)

driver.quit()