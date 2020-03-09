import requests

keyword = input('请输入搜索内容:')
try:
    kw = {'wd' : keyword}
    r = requests.get('https://www.baidu.com/s', headers = { 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}, params = kw)
    #r = requests.get('https://www.baidu.com/s', headers = { 'Accept' : 'text/html, application/xhtml+xml, */*', 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}, params = kw)
    print(r.request.url)
    r.raise_for_status() 
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('搜索失败')
