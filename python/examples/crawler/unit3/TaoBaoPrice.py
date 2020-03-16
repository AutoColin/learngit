import requests
import re 

def getHtml(url):
    http_head = {'user-agent' : '你的浏览器信息'}
    cook = {'cookie' : '你的cookie'}
    try:
        r = requests.get(url, timeout = 30, headers = http_head, cookies = cook)
        r.raise_for_status()
        r.encoding = r.apparent_encoding 
        return r.text
    except:
        print('Html page receiving error!')

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  #商品价格
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)       #商品全称
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('Html page parsing error')

def printItemsList(ilt):
    mod = '{:4}\t{:8}\t{:16}'
    print(mod.format('序号','价格','商品名称'))
    count = 0
    for i in ilt:
        count += 1
        print(mod.format(count, i[0], i[1]))

def main():
    #item = '肩带'
    item = input('请输入要查询的商品:')
    #depth = 3
    depth = eval(input('请输入要查询的页面数:'))
    start_url = 'https://s.taobao.com/search?q=' + item
    itemsList=[]
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHtml(url)
            parsePage(itemsList, html)
        except:
            continue
    printItemsList(itemsList)

main()
