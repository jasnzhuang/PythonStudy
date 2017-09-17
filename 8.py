import requests
from bs4 import BeautifulSoup
import bs4


# 获取网页信息的通用框架
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '爬取失败'


# 填充列表
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'lxml')
    for tr in soup.find('tbody').children:
        # 检查网页代码可以发现数据都储存在tboyd标签中，这里需要对tbody的儿子节点进行遍历
        if isinstance(tr, bs4.element.Tag):
            # 检测标签类型，如果不是bs4库支持的Tag类型，就过滤掉，这里需要先导入bs4库
            tds = tr('td')
            # 解析出tr标签中的td标签后，将其储存在列表tds中
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
            # 我们需要的是排名、学校名称和总分


# 格式化后，输出列表数据
def printUnivList(ulist, num):
    tplt = '{:<10}\t{:<10}\t{:<10}'
    # 定义输出模板为变量tplt，\t为横向制表符，<为左对齐，10为每列的宽度
    print(tplt.format('排名', '学校名称', '总分'))
    # format()方法做格式化输出
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2]))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10)
    # 选取前10所学校信息


main()
