import requests
import urllib3
r = requests.get('http://hdjwweb.jzyqzypg.com/cache/getProductList?_t_=1590504446862&packageName=%E5%B0%8F%E5%AD%A6%E5%9B%9B%E5%B9%B4%E7%BA%A7%E8%8B%B1%E8%AF%AD&pn=1&tabType=6&tabName=%E7%A9%BA%E4%B8%AD%E8%AF%BE%E5%A0%82&userName=1317422978&productName=')
productList = r.json()["data"]["productList"]
print(type(productList))
for i in range(len(productList)):
    url = productList[i]["thumb"]
    url = url.replace("png/transform.png", "mp4/transform.mp4")
    name = productList[i]["productName"]
    # print(name)
    # urllib.request.urlretrieve(url, "/Users/xiao/Documents/空中课堂/数学/" + name)

    r = requests.get(url)
    with open("/Users/xiao/Documents/空中课堂/英语/" + name, "wb") as code:
        code.write(r.content)
        print("download " + name)

