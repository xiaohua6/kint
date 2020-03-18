import json
import execjs
import re
import requests

# 循环获取想要翻译的语句
while True:
    # 定义想要翻译的语句
    string = input('请输入要翻译的句子：')
    # 定义从英语翻译成中文
    from1, to = ("en", 'zh')

    # 正则查看输入的字符串饱不包含中文，如果包含则定义从英文翻译成中文
    if re.match('[\u4E00-\u9FA5]+', string):
        from1, to = ("zh", 'en')

    # 获取生成的sign值
    with open('baidufanyi.js', 'r', encoding='utf-8') as f:
        exc = execjs.compile(f.read())
    sign = exc.call('e', string)
    print(sign)

    # 定义提交数据
    data = {"from": from1, "to": to, "query": string, "simple_means_flag": 3, "sign": sign,
            "token": "6461856d74c54e85d770abb0d07ab37c"}

    # 定义请求头
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.3",
        "cookie": "BAIDUID=CA0CEFC83D57A8BA9CCB88F424A832BA:FG=1; PSTM=1568773645; BIDUPSID=6BAAD3B1C9F8F2F8EFF78EC26593F720; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1573259604,1573269113; H_PS_PSSID=1422_21123_29568_29220_26350; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1573269009,1573276142,1573279062,1573316651; yjs_js_security_passport=b11e2930d9ae214e9a96c2a516960fb4fa0c336a_1573317006_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1573317167; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; __yjsv5_shitong=1.0_7_1676d21b1f5ebdbd0672f4f3a1222a724a9d_300_1573317172549_223.104.147.79_31aad5a3"}

    # 获取响应结果
    response = requests.post(url='https://fanyi.baidu.com/v2transapi?from=en&to=zh', headers=headers, data=data)

    # 获取响应结果
    result = json.loads(response.content.decode())

    # 打印翻译结果
    print(result['trans_result']['data'][0]['dst'])
