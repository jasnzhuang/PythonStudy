import re
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

news = 'http://news.sina.com.cn/o/2017-05-13/doc-ifyfekhi7537438.shtml'
commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'


def getCommentCount(newsurl):
    m = re.search('doc-i(.+).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']


def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newssource'] = soup.select('.time-source span a')[0].text
    timesource = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource, '%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
    result['comments'] = getCommentCount(newsurl)
    return result


print(getNewsDetail('http://news.sina.com.cn/o/2017-05-13/doc-ifyfekhi7537438.shtml'))
print(getCommentCount('http://news.sina.com.cn/o/2017-05-13/doc-ifyfekhi7537438.shtml'))
