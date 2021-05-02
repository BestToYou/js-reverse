import requests
url ="http://match.yuanrenxue.com/match/2"

rs  =requests.get(url = url)
print(rs.text)