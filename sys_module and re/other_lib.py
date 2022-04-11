"""
第三方：pillow pip  install pillow(python成像库)

"""
import requests

response = requests.get("http://www.12306.cn/")
print(response.text)

