import requests
from time import sleep
import random
import requests
import json
from time import sleep

def getIP(): #返回ip供两个线程使用
    targetUrl = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=be8ff80b6a1a48cda1918a17a72d3390&count=1&expiryDate=0&format=2&newLine=3'

    resp = requests.get(targetUrl)
    print(resp.status_code)
    if 'code' in resp.text:
        sleep(1)
        return getIP()
    # print(resp.text)
    item=resp.text.split('\n')
    print(item)
    proxy_http="http://{}".format(item[0])
    proxy_https="https://{}".format(item[0])
    proxies={"http":proxy_http,"https":proxy_https}
    if check(proxies)==1 and resp.status_code==200:
        print('return')
        return proxies
    else:
        sleep(3)
        return getIP()


#检查ip是否有效
def check(proxies):
    date='2020-01-01'
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    ]
    user_agent = (random.choice(USER_AGENT_LIST))

    request_headers={
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'content-length': '287',
    'content-type': 'application/json',
    'cookie': '_abtest_userid=427f44ed-cf0b-4c75-b995-b4ca21d572fe; _ga=GA1.2.1406023646.1573299831; _RF1=111.207.1.146; _RSG=7_aiNPEaVwC1J9izn1bcvA; _RDG=28a1df2533a37725e23e1a74ab64575ae6; _RGUID=ce9f90e6-57b2-4fc7-ae66-941c7db094c1; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; appFloatCnt=5; _gid=GA1.2.1669130808.1575119640; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242019-12-4%24%u5357%u5B81%28%u5434%u5729%u56FD%u9645%u673A%u573A%29%28NNG%29%24NNG%24%24%24"}; _bfa=1.1573299825075.2c2710.1.1574130278578.1575119584536.9.82; _bfs=1.3; _jzqco=%7C%7C%7C%7C%7C1.51473978.1573299831438.1575119640308.1575119698012.1575119640308.1575119698012.0.0.0.65.65; __zpspc=9.10.1575119640.1575119698.2%233%7Cwww.google.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D100101991%26v1%3D82%26v2%3D81',
    # '_abtest_userid=427f44ed-cf0b-4c75-b995-b4ca21d572fe; _ga=GA1.2.1406023646.1573299831; _RF1=111.207.1.146; _RSG=7_aiNPEaVwC1J9izn1bcvA; _RDG=28a1df2533a37725e23e1a74ab64575ae6; _RGUID=ce9f90e6-57b2-4fc7-ae66-941c7db094c1; appFloatCnt=5; _gid=GA1.2.1669130808.1575119640; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5929%u6D25%28TSN%29%24TSN%242019-12-6%24%u6842%u6797%28%u4E24%u6C5F%u56FD%u9645%u673A%u573A%29%28KWL%29%24KWL%24%24%24"}; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4899&SID=135371&OUID=&Expires=1575899547197; _bfa=1.1573299825075.2c2710.1.1575294741108.1575297977128.19.101; _bfs=1.2; _jzqco=%7C%7C%7C%7C%7C1.51473978.1573299831438.1575297980376.1575298473075.1575297980376.1575298473075.0.0.0.83.83; __zpspc=9.20.1575297980.1575298473.2%233%7Cwww.google.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D101%26v2%3D99',
    'origin': 'https://flights.ctrip.com',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/tsn-kwl?date={}'.format(str(date)),
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'Connection': 'close',
    'user-agent': user_agent,
    }

    #request payload
    data={"flightWay":"Oneway",
        "classType":"ALL",
        "hasChild":'false',
        "hasBaby":'false',
        "searchIndex":1,
        "date":str(date),
        "airportParams":[{"dcity":"TSN","acity":"KWL","dcityname":"天津","acityname":"桂林","date":str(date),"dcityid":3,"acityid":33}],
        "token":"afdf8bc932b8724d47bb9a7ce9014441"
    }

    url='https://flights.ctrip.com/itinerary/api/12808/products' # 真正的请求链接

    try:
        r=requests.post(url,headers=request_headers,data=json.dumps(data),proxies=proxies).json()
    except:
        print('无效ip')
        return 0

    # print(r)
    if len(r)==2:
        print('无效ip')
        return 0
    else:
        print('有效ip')
        return 1

        
    
    
