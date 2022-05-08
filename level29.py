import requests, bz2

url = "http://www.pythonchallenge.com/pc/ring/guido.html"
r = requests.get(url, auth=("repeat", "switch"))
msg = [len(i) for i in r.text.split("\n")[12:]]
print(bz2.decompress(bytes(msg)))