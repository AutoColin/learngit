import requests

keyword = input('请输入搜索内容:')
try:
    kw = {'q' : keyword}
    r = requests.get('https://www.so.com/s', params = kw)
    print(r.request.url)
    r.raise_for_status() 
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('搜索失败')
