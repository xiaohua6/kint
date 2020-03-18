import re
import requests
import time

num2=1
for num1 in range(1,12):

    # url='https://www.meizitu.com/a/xiaoqingxin_6_%d.html'%num1
    url='https://www.meizitu.com/a/xinggan_2_%d.html'%num1

    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
    response=requests.get(url,headers=headers)

    response=response.content.decode("GBK")

    result_image=re.findall('img src="(.*\.jpg)"',response)


    for image_url in result_image:

        image=requests.get(image_url,headers=headers)

        with open('xinggan/%d.jpg'% num2,'wb') as f:
            f.write(image.content)
            num2+=1

        time.sleep(2)


