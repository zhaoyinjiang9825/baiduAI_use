import requests
import json
import time
App_Key = 'IPI5sjmvuGPpbqLEkiphlALa'
Secret_Key = 'gUWWR41kuDx8b3GWkZBYiQHNp6g5FY2h'


# 情感分析
def getEmotion(inputText, access_token):
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=' + access_token
    header = {'Content-Type	': 'application/json'}
    body = {'text': inputText}
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url=url, data=json.dumps(body), headers=header, verify=False)

    #  返回接口格式：
    # {
    #     "log_id": 7475291888689599393,    # 请求唯一标识码
    #     "text": "我最好看",               #
    #     "items": [
    #         {
    #             "positive_prob": 0.999976,   # 表示属于积极类别的概率 ，取值范围[0,1]
    #             "confidence": 0.999946,       # 表示分类的置信度，取值范围[0,1]
    #             "negative_prob": 2.42354e-05,  # 表示属于消极类别的概率，取值范围[0,1]
    #             "sentiment": 2             # 表示情感极性分类结果，0:负向，1:中性，2:正向
    #         }]
    # }

    if res.status_code == 200:
        info = json.loads(res.text)
        print(info)
        if 'items' in info and len(info['items']) > 0:
            sentiment = info['items'][0]['sentiment']
            if sentiment == 2:
                t=inputText + ' |正向'
                with open(r'G:\projeict_item\百度AI接口调用\data\output_doc\positive_result.txt','a',encoding='UTF-8') as b1:
                    b1.write(t+'\n')
                print(t)
            elif sentiment == 1:
                t=inputText + ' |中性'
                with open(r'G:\projeict_item\百度AI接口调用\data\output_doc\neutral_result.txt','a',encoding='UTF-8') as b2:
                    b2.write(t+'\n')
                print(t)
            else:
                t=inputText + ' |负向'
                with open(r'G:\projeict_item\百度AI接口调用\data\output_doc\negative_result.txt','a',encoding='UTF-8') as b3:
                    b3.write(t+'\n')
                print(t)



# 获取token
def getToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + App_Key + '&client_secret=' + Secret_Key
    response = requests.get(host)

    if response.status_code == 200:
        info = json.loads(response.text)  # 将字符串转成字典
        access_token = info['access_token']  # 解析数据到access_token
        return access_token
    return ''


# 主函数
def main():
    file_path='G:\projeict_item\百度AI接口调用\data\测试文档.txt'
    f=open(file_path,'r',encoding='UTF-8').readlines()
    for line in f:
        str=line.replace('\n','')
        #inputText = input('请输入需要分析的语句:')
        inputText = str
        accessToken = getToken()
        getEmotion(inputText, accessToken)
        time.sleep(0.5)


if __name__ == '__main__':
    main()