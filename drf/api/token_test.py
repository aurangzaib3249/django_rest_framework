import requests

url="http://127.0.0.1:8000"
res=requests.get(url)
print(res.text)
header={"Authorization":'Token e6f8dc883a814661e636b83b1cf2da06f8ac8be6'}
res=requests.get(url,headers=header)


print(res.text)