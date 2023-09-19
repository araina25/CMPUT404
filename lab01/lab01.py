import requests

url = "https://raw.githubusercontent.com/araina25/CMPUT404/main/lab01/lab01.py"
res = requests.get(url)

print(res.text)



