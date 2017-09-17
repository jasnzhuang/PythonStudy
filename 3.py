import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()
http = urllib3.PoolManager()
r = http.request('GET',
                 'http://www.iplaysoft.com',
                 headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
                 })

print(r)
# soup = BeautifulSoup(r.data, 'html.parser')
soup = BeautifulSoup(r.data, 'html5lib')
title = soup.select('.entry-title')
for link in title:
    print(link.text)
