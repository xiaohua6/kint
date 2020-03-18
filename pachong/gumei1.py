import requests



response=requests.get('https://reg.gome.com.cn/register/index/person?intcmp=sy-public01003')
print(response.content.decode('utf-8'))