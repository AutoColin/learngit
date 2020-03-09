import requests

keyword = input('请输入IP地址:')
try:
    r = requests.get('https://www.ip138.com/iplookup.asp?ip=' + keyword + '&action=2',\
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'})
    r.raise_for_status()
    r.encoding = r.apparent_encoding 
    print(r.text)
except:
    print('爬取失败')
