import requests
haeders ={
'Host': 'match.yuanrenxue.com',
'Connection': 'keep-alive',
'Content-Length': '0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0',
'Accept': '*/*',
'Origin': 'http://match.yuanrenxue.com',
'Referer': 'http://match.yuanrenxue.com/match/3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
}
session = requests.session()
session.headers= haeders
logoUrl = "http://match.yuanrenxue.com/logo"
rs = session.post(logoUrl)
rs = session.get("http://match.yuanrenxue.com/api/match/3")
print(rs.text)
