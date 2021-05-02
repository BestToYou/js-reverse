import execjs
import requests


with open('encryption.js', 'r', encoding='utf-8') as f:
    docjs = execjs.compile(f.read())
    res = docjs.call('test')
    print(res)



headers  ={

'Host': 'match.yuanrenxue.com',
'Referer': 'http://match.yuanrenxue.com/match/1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
}

url = 'http://match.yuanrenxue.com/api/match/1?page=1&m={}'.format(res)

print(url)
data = requests.get(url=url,headers=headers)
print(data.text)

