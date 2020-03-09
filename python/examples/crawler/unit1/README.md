经过测试发现百度的请求头里必须有accept和user-agent信息,而且accept信息似乎得满足一定条件,伪装程度有一定要求,否则会触发百度的反爬虫机制,下面那行的accept是不行的,但是accept-language,accept-encoding,connection等其他信息貌似都不会进行检测  

360搜索并没有简单的反爬虫:joy:  

138的IP地址查询需要加上user-agent信息
