import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHtml(url, code = 'utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('Html page receiving error!')

def getStockList(lst, stockUrl):
    html = getHtml(stockUrl, 'GB2312')
    soup = BeautifulSoup(html, 'lxml')
    tag = soup.find_all('a')
    for i in tag:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]_\d{6}', href)[0][-6:])
        except:
            continue

def getStockInfo(lst, stockUrl, fPath):
    count = 0
    for stock in lst:
        queryUrl = stockUrl + stock + '.html'
        html = getHtml(queryUrl)
        try:
            if html == '':
                print('url blank')
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'lxml')

            name = soup.find_all('div', attrs = {'class' : 'Lfont'})[0]
            value = soup.find_all('span', attrs = {'id' : 'last'})[0]
            #infoDict.update({'股票名称' : [name.string[:-8], value.string[:-1]]})
            infoDict.update({name.string : value.string})

            with open(fPath, 'a', encoding = 'utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print('\r当前进度:{:.2f}%'.format(count * 100 / len(lst)), end = '')
        except:
            count += 1
            print('\r当前进度:{:.2f}%'.format(count * 100 / len(lst)), end = '')
            continue

def main():
    stock_list_url = 'https://quote.stockstar.com/stock/stock_index.htm'
    stock_info_url = 'http://quote.cfi.cn/'
    output_file = './StockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
