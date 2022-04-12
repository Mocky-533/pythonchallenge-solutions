# section 1
import re, bz2, urllib, requests
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
r=requests.get(url)
txt=r.text
cookies = r.cookies['info']
while True:
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+txt.split()[-1]
    r=requests.get(url)
    txt = r.text
    print(txt)
    print(r.cookies['info'])
    cookies += r.cookies['info']
    result = re.search('the next busynothing is (\d+)', txt)
    if result == None:
        break
line = urllib.parse.unquote_to_bytes(cookies)
print(bz2.decompress(line).decode("utf-8"))

# section 2
import xmlrpc.client
post = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(post.phone("Leopold"))

# section 3
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
headers = {'Cookie':'info=the flowers are on their way'}
r = requests.get(url, headers=headers)
print(r.text)