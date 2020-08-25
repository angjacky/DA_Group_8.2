import requests
url = 'http://172.18.58.238/nantes/'
r = requests.get(url)
print("Status code:")
print("\t *", r.status_code)
h = requests.head(url)
print("Nantes")
print("----get----")
for x in h.headers:
    print("\t ", x, ".", h.headers[x])
print("----OK----")
headers = { 'User-Agent' : 'Mobile'}
url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)