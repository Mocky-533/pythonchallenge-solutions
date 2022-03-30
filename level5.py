from urllib import request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
f = request.urlopen(url)
result = pickle.load(f)
print(result)

for i in result:
    for j in i:
        print(j[0] * j[1], end = '')
    print('\n')