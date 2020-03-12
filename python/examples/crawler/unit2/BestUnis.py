import requests
from bs4 import BeautifulSoup
import bs4

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('url parsing error!')

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            #tds = tr('td')
            tds = tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    mod = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(mod.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        l = ulist[i]
        print(mod.format(l[0], l[1], l[2], chr(12288)))

def main():
    unifo = []
    url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHtml(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)

main()
