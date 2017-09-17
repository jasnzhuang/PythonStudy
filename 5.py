# 这个是无差别的把地址页面中A标签的href属性和inner text都提取出来
import requests
from bs4 import BeautifulSoup
import re


# 下一步思路，写个判断，用match判断是什么类型的新闻，然后读取相应不同位置的信息内容
def getnewstitle(url):
    tres = requests.get(url)
    vnews = re.match(url, 'http://v.qq.com.*')
    news = re.match(url, 'http://news.qq.com/a/\d{8}/\d{6}.htm')
    notnews = re.match(url, '^(?:(?!\bhttp://news.qq.com/a/\d{8}/\d{6}.htm\b).)*$')
    if news:
        tres.encoding = 'gbk'
        print('true')
    tsoup = BeautifulSoup(tres.text, 'html.parser')
    print(tsoup.head.title.string)
    print(url)
    return


res = requests.get('http://news.qq.com')
res.encoding = 'gbk'
soup1 = BeautifulSoup(res.text, 'html.parser')
soup = soup1.select('.con')
# print(soup)
# 取得href的内容和inner text的内容的re
# regex = "<a.+?href=\"(.+?)\".*>(.+)</a>"
# 取得仅仅href内容的re
# regex = "<a.+?href=\"(.+?)\".*></a>"
# 取得仅仅inner text内容的re
# regex = "<a.+?href=\".*\".*>(.+)</a>"
# 之前的不去分辨链接是否为http，现在加个
# regex = "<a.+?href=\"(http.+?)\".*>(.+)</a>"
# 结合上面那条，只要包含http的a href的内容
# regex = "<a.+?href=\"(http.+?)\".*></a>"
# 继续更，因为在inner text里面居然抓出了图片链接，为了去掉他们(not finished)
# regex = "<a.+?href=\"(http.+?)\".*>(.+)</a>"
# 临时测试用的简单写法
# regex = 'http://news.qq.com/a/\d{8}/\d{6}.htm'
# 这种用法之下，content的类型是list
regex = '<a.+?href=\"(http://news.qq.com/a/\d{8}/\d{6}.htm)\".*></a>'
content = re.findall(regex, str(soup))
# print(content)
# print(type(content))
for i in content:
    # print(i)
    getnewstitle(i)
# print(type(i))
