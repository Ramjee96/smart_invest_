import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://m.stock.naver.com/item/main.nhn#/stocks/144510/total',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

rates = soup.select('#header.renewal_header._header> div.end_header_topinfo> div.flick-container.major_info_wrp> div>div>div>div.stock_info>div.elips_wrp._stock_name')

for rates_info in rates:
    name = rates_info.select_one('h2.elips').text

    print(name)
