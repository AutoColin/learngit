import requests
from bs4 import BeautifulSoup

try:
    url = 'https://python123.io/ws/demo.html'
    r = requests.get(url)
    r.raise_for_status()
    page = BeautifulSoup(r.text, 'lxml')
    #print(page.prettify())
    for p in page.a.previous_siblings:
        if p is None:
            print(p)
        else:
            print(p)
except:
    print('something goes wrong!')
