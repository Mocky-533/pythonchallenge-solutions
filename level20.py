import requests, base64

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
cred = base64.b64encode(b"butter:fly")
requests.auth.HTTPBasicAuth("butter", "fly")
headers = {'Authorization': f"Basic {cred.decode()}", 'Range':'bytes=1152983631-'}
r = requests.get(url, headers=headers)
print(r.headers)
with open('assets/21.zip', 'wb') as f: # file is actually the content of Level 21
    f.write(r.content)
# print(r.content[:20])
