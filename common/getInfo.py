# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import datetime
from dateutil.relativedelta import relativedelta
import re
from bs4 import BeautifulSoup
import requests
import json
from save2sql import Tosql
from getIP import getIP,check
import threading

#城市代码
city={'阿尔山': 'YIE', '阿克苏': 'AKU', '阿拉善右旗': 'RHT', '阿拉善左旗': 'AXF', '阿勒泰': 'AAT', '阿里': 'NGQ', '澳门': 'MFM',
            '安庆': 'AQG', '安顺': 'AVA', '鞍山': 'AOG', '巴彦淖尔': 'RLK', '百色': 'AEB', '包头': 'BAV', '保山': 'BSD', '北海': 'BHY',
            '北京': 'BJS', '白城': 'DBC', '白山': 'NBS', '毕节': 'BFJ', '博乐': 'BPL', '重庆': 'CKG', '昌都': 'BPX', '常德': 'CGD',
            '常州': 'CZX', '朝阳': 'CHG', '成都': 'CTU', '池州': 'JUH', '赤峰': 'CIF', '揭阳': 'SWA', '长春': 'CGQ', '长沙': 'CSX',
            '长治': 'CIH', '承德': 'CDE', '沧源': 'CWJ', '达县': 'DAX', '大理': 'DLU', '大连': 'DLC', '大庆': 'DQA', '大同': 'DAT',
            '丹东': 'DDG', '稻城': 'DCY', '东营': 'DOY', '敦煌': 'DNH', '芒市': 'LUM', '额济纳旗': 'EJN', '鄂尔多斯': 'DSN', '恩施': 'ENH',
            '二连浩特': 'ERL', '佛山': 'FUO', '福州': 'FOC', '抚远': 'FYJ', '阜阳': 'FUG', '赣州': 'KOW', '格尔木': 'GOQ', '固原': 'GYU',
            '广元': 'GYS', '广州': 'CAN', '贵阳': 'KWE', '桂林': 'KWL', '哈尔滨': 'HRB', '哈密': 'HMI', '海口': 'HAK', '海拉尔': 'HLD',
            '邯郸': 'HDG', '汉中': 'HZG', '杭州': 'HGH', '合肥': 'HFE', '和田': 'HTN', '黑河': 'HEK', '呼和浩特': 'HET', '淮安': 'HIA',
            '怀化': 'HJJ', '黄山': 'TXN', '惠州': 'HUZ', '鸡西': 'JXA', '济南': 'TNA', '济宁': 'JNG', '加格达奇': 'JGD', '佳木斯': 'JMU',
            '嘉峪关': 'JGN', '金昌': 'JIC', '金门': 'KNH', '锦州': 'JNZ', '嘉义': 'CYI', '西双版纳': 'JHG', '建三江': 'JSJ', '晋江': 'JJN',
            '井冈山': 'JGS', '景德镇': 'JDZ', '九江': 'JIU', '九寨沟': 'JZH', '喀什': 'KHG', '凯里': 'KJH', '康定': 'KGT', '克拉玛依': 'KRY',
            '库车': 'KCA', '库尔勒': 'KRL', '昆明': 'KMG', '拉萨': 'LXA', '兰州': 'LHW', '黎平': 'HZH', '丽江': 'LJG', '荔波': 'LLB',
            '连云港': 'LYG', '六盘水': 'LPF', '临汾': 'LFQ', '林芝': 'LZY', '临沧': 'LNJ', '临沂': 'LYI', '柳州': 'LZH', '泸州': 'LZO',
            '洛阳': 'LYA', '吕梁': 'LLV', '澜沧': 'JMJ', '龙岩': 'LCX', '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '漠河': 'OHE',
            '牡丹江': 'MDG', '马祖': 'MFK', '南昌': 'KHN', '南充': 'NAO', '南京': 'NKG', '南宁': 'NNG', '南通': 'NTG', '南阳': 'NNY',
            '宁波': 'NGB', '宁蒗': 'NLH', '攀枝花': 'PZI', '普洱': 'SYM', '齐齐哈尔': 'NDG', '黔江': 'JIQ', '且末': 'IQM', '秦皇岛': 'BPE',
            '青岛': 'TAO', '庆阳': 'IQN', '衢州': 'JUZ', '日喀则': 'RKZ', '日照': 'RIZ', '三亚': 'SYX', '厦门': 'XMN', '上海': 'SHA',
            '深圳': 'SZX', '神农架': 'HPG', '沈阳': 'SHE', '石家庄': 'SJW', '塔城': 'TCG', '台州': 'HYN', '太原': 'TYN', '扬州': 'YTY',
            '唐山': 'TVS', '腾冲': 'TCZ', '天津': 'TSN', '天水': 'THQ', '通辽': 'TGO', '铜仁': 'TEN', '吐鲁番': 'TLQ', '万州': 'WXN',
            '威海': 'WEH', '潍坊': 'WEF', '温州': 'WNZ', '文山': 'WNH', '乌海': 'WUA', '乌兰浩特': 'HLH', '乌鲁木齐': 'URC', '无锡': 'WUX',
            '梧州': 'WUZ', '武汉': 'WUH', '武夷山': 'WUS', '西安': 'SIA', '西昌': 'XIC', '西宁': 'XNN', '锡林浩特': 'XIL',
            '香格里拉(迪庆)': 'DIG',
            '襄阳': 'XFN', '兴义': 'ACX', '徐州': 'XUZ', '香港': 'HKG', '烟台': 'YNT', '延安': 'ENY', '延吉': 'YNJ', '盐城': 'YNZ',
            '伊春': 'LDS',
            '伊宁': 'YIN', '宜宾': 'YBP', '宜昌': 'YIH', '宜春': 'YIC', '义乌': 'YIW', '银川': 'INC', '永州': 'LLF', '榆林': 'UYN',
            '玉树': 'YUS',
            '运城': 'YCU', '湛江': 'ZHA', '张家界': 'DYG', '张家口': 'ZQZ', '张掖': 'YZY', '昭通': 'ZAT', '郑州': 'CGO', '中卫': 'ZHY',
            '舟山': 'HSN',
            '珠海': 'ZUH', '遵义(茅台)': 'WMT', '遵义(新舟)': 'ZYI'}

#城市代号
city_num={
    '北京':1, '天津':3, '石家庄':428, '南宁':380, '桂林':33, '梧州':492, '柳州':354, '北海':189,
}

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
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]


proxies1=getIP()
sleep(3)
proxies2=getIP() #全局可以改变的ip
s1,s2=0,0 #全局判断每个ip使用次数，为了防止被封，使用50次更换
end1,end2=1,1 #判断两个爬取线程结束的全局变量

# 根据出发地，目的地，时间爬取，只爬取飞机，不中转
def info_search(url:str,start:str,end:str,date,proxies):
    # print(str(date))
    date_time=str(datetime.datetime.strptime(str(date),'%Y-%m-%d')) # 转换为日期
    week_day=date.strftime('%w') # 转换为周几
    week_dict={'0':'周日','1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周六'}
    week_day=week_dict[week_day]
    
    user_agent = (random.choice(USER_AGENT_LIST))

    # # headers
    # pre_headers={
    #     'User-Agent': user_agent,
    #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #    'accept-encoding':'gzip, deflate, br',
    #    'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    #    'cache-control':'max-age=0',
    #    'cookie':'_abtest_userid=427f44ed-cf0b-4c75-b995-b4ca21d572fe; _ga=GA1.2.1406023646.1573299831; _RF1=111.207.1.146; _RSG=7_aiNPEaVwC1J9izn1bcvA; _RDG=28a1df2533a37725e23e1a74ab64575ae6; _RGUID=ce9f90e6-57b2-4fc7-ae66-941c7db094c1; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; appFloatCnt=5; _gid=GA1.2.1669130808.1575119640; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242019-12-4%24%u5357%u5B81%28%u5434%u5729%u56FD%u9645%u673A%u573A%29%28NNG%29%24NNG%24%24%24"}; _bfa=1.1573299825075.2c2710.1.1574130278578.1575119584536.9.82; _bfs=1.3; _jzqco=%7C%7C%7C%7C%7C1.51473978.1573299831438.1575119640308.1575119698012.1575119640308.1575119698012.0.0.0.65.65; __zpspc=9.10.1575119640.1575119698.2%233%7Cwww.google.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D100101991%26v1%3D82%26v2%3D81',
    #    'Referer': 'https://www.ctrip.com/',
    # }

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
        "airportParams":[{"dcity":city[start],"acity":city[end],"dcityname":start,"acityname":end,"date":str(date),"dcityid":city_num[start],"acityid":city_num[end]}],
        "token":"afdf8bc932b8724d47bb9a7ce9014441"
    }
    url='https://flights.ctrip.com/itinerary/api/12808/products' # 真正的请求链接
    # print(url)
    while 1:
        try:
            r=requests.post(url,headers=request_headers,data=json.dumps(data),proxies=proxies).json()
            while len(r)==2: #请求失败后更换重新搜索
                proxies=getIP()
                sleep(random.choice([0.1,0.8,1.1]))
                r=requests.post(url,headers=request_headers,data=json.dumps(data),proxies=proxies).json()
            return r
        except:
            proxies=getIP()

    # print(r)
    
#获取未来1个月的日期
def getDate(today):
    dates=[]
    begin=today+ datetime.timedelta(days=1)
    end=begin+relativedelta(months=+1)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        dates.append(day)
    return dates

#获取信息解析后插入db
def insert(flag,departure,destination,dates,tosql):
    global s1,s2,end1,end2,proxies1,proxies2
    if flag: #爬取去程
        for on in departure:
            for off in destination:
                for date in dates:
                    a=0 #防止丢包
                    while a<5:
                        # print(on,off,str(date))
                        data=info_search('https://flights.ctrip.com/itinerary/oneway/',on,off,date,proxies1)
                        s1+=1
                        if data['data']['routeList']!=None:
                            print(on,off,str(date),"当日有航班")
                            print(data['data']['routeList'])
                            # parseInfo(data)
                            # tosql.insert(search_list)
                            print(len(data))
                            # print(search_list)
                            break
                        else:
                            a+=1
                    if a==5:
                        print(on,off,str(date),"当日没有航班")
                    sleep(random.choice([0.8,1,1.1,1.5,1.7,2.2]))
        end1=0
    else: #爬取返程
        for on in departure:
            for off in destination:
                for date in dates:
                    a=0 #防止丢包
                    while a<5:
                        # print(on,off,str(date))
                        data=info_search('https://flights.ctrip.com/itinerary/oneway/',off,on,date,proxies2)
                        s2+=1
                        if data['data']['routeList']!=None:
                            print(on,off,str(date),"当日有航班")
                            print(data['data']['routeList'])
                            # parseInfo(data)
                            # tosql.insert(search_list)
                            print(len(data))
                            # print(search_list)
                            break
                        else:
                            a+=1
                    if a==5:
                        print(off,on,str(date),"当日没有航班")
                    sleep(random.choice([0.8,1,1.1,1.5,1.7,2.2]))
        end2=0

def parseInfo(data):
    print(data['data']['routeList'])




def changeIP(): #根据要求改变ip
    global s1,s2,proxies1,proxies2,end1,end2
    while end1 and end2:
        # print('s1 s2:','\n',s1,s2)
        if s2>=20:
            s2=0
            proxies2=getIP()
            print(proxies2,'\n')
        if s1>=35:
            s1=0
            proxies1=getIP()
            print(proxies1,'\n')

if __name__ == '__main__':
    clear_flag=1
    tosql=Tosql(clear_flag)
    departure=['天津','北京','石家庄']  # 出发地 
    destination=['南宁','桂林','梧州','柳州','北海'] # 目的地 
    dates=getDate(datetime.date.today()) # 日期
    t1 = threading.Thread(target=insert,name='to',args=(1,departure,destination,dates,tosql)) #爬去去程
    t2 = threading.Thread(target=insert,name='back',args=(0,departure,destination,dates,tosql)) #爬去返程
    t3 = threading.Thread(target=changeIP,name='ip') #改变ip的线程
    t3.start()
    t1.start()
    t2.start()
    t3.join()
    t1.join()
    t2.join()

