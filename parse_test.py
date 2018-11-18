import urllib.request
import urllib.parse
import re

url = 'https://www.basketball-reference.com/boxscores/'
values = {'s':'basics','sumbmit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

# paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
#
# for eachP in paragraphs:
#     print(eachP)
