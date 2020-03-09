import requests
import bs4

def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding 
        #return r.text 
        return bs4.BeautifulSoup(r.text, 'html.parser').prettify() 
    except:
        return '请求URL输入错误或目标地址异常'

if __name__ == '__main__':
    url = 'https://' + input('请输入目标URL:')
    print(getHtmlText(url))
