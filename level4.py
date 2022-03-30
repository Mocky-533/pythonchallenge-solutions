import requests
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
r=requests.get(url)
txt=r.text
for i in range(260):
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+txt.split()[-1]
    r=requests.get(url)
    txt=r.text
    print(txt)