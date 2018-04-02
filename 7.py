import re
from bs4 import BeautifulSoup
import requests

# url = 'http://news.sina.com.cn/china/'
# web_data = requests.get(url)
# web_data.encoding = 'utf-8'
# soup = BeautifulSoup(web_data.text, 'lxml')
# for news in soup.select('.news-item'):
#     if len(news.select('h2')) > 0:
#         h2 = news.select('h2')[0].text
#         time = news.select('.time')[0].text
#         a = news.select('a')[0]['href']
#         print(h2)
#         print(time)
#         print(a)
url = 'https://s.taobao.com/search?q=%E6%B1%9F%E5%B4%9F%E6%89%8D%E6%98%AF%E5%82%BB%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&ie=utf8&initiative_id=tbindexz_20170306'
tb_data = requests.get(url)
tb_data.encoding = 'utf-8'
soup = BeautifulSoup(tb_data.text, 'lxml')
re_h=re.compile('</?\w+[^>]*>')#HTML标签
#
# for item in soup.select('.items'):
#
#     if
#         s=re_h.sub('',s) #去掉HTML 标签
print(tb_data)
print(tb_data.text)