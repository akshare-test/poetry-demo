import requests

url = "https://www.baidu.com"
r = requests.get(url)
data_text = r.text
print(data_text)
# add test
