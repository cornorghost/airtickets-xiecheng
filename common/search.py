from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import datetime
from dateutil.relativedelta import relativedelta
import re
from save2sql import Tosql

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

# 根据出发地，目的地，时间爬取，只爬取飞机，不中转
def info_search(url:str,start:str,end:str,date):
    print(str(date))
    date_time=str(datetime.datetime.strptime(str(date),'%Y-%m-%d')) # 转换为日期
    week_day=date.strftime('%w') # 转换为周几
    week_dict={'0':'周日','1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周六'}
    week_day=week_dict[week_day]
    info_list=[]
    chrome_options=Options()
    #设置chrome浏览器无界面模式
    chrome_options.add_argument('--headless')
    #构建headers
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
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)']
    user_agent = (random.choice(USER_AGENT_LIST))
    headers = 'User-Agent= "{}",Accept="{}",accept-encoding="{}",accept-language="{}",cache-control="{}",cookie="{}",Referer="{}"'.format(user_agent,
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'gzip, deflate, br',
    'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'max-age=0',
    '_abtest_userid=427f44ed-cf0b-4c75-b995-b4ca21d572fe; _ga=GA1.2.1406023646.1573299831; _RF1=111.207.1.146; _RSG=7_aiNPEaVwC1J9izn1bcvA; _RDG=28a1df2533a37725e23e1a74ab64575ae6; _RGUID=ce9f90e6-57b2-4fc7-ae66-941c7db094c1; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; appFloatCnt=5; _gid=GA1.2.1669130808.1575119640; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242019-12-4%24%u5357%u5B81%28%u5434%u5729%u56FD%u9645%u673A%u573A%29%28NNG%29%24NNG%24%24%24"}; _bfa=1.1573299825075.2c2710.1.1574130278578.1575119584536.9.82; _bfs=1.3; _jzqco=%7C%7C%7C%7C%7C1.51473978.1573299831438.1575119640308.1575119698012.1575119640308.1575119698012.0.0.0.65.65; __zpspc=9.10.1575119640.1575119698.2%233%7Cwww.google.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D100101991%26v1%3D82%26v2%3D81',
    'https://www.ctrip.com/')

    #    'User-Agent': user_agent,
    #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #    'accept-encoding':'gzip, deflate, br',
    #    'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    #    'cache-control':'max-age=0',
    #    'cookie':'_abtest_userid=427f44ed-cf0b-4c75-b995-b4ca21d572fe; _ga=GA1.2.1406023646.1573299831; _RF1=111.207.1.146; _RSG=7_aiNPEaVwC1J9izn1bcvA; _RDG=28a1df2533a37725e23e1a74ab64575ae6; _RGUID=ce9f90e6-57b2-4fc7-ae66-941c7db094c1; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; appFloatCnt=5; _gid=GA1.2.1669130808.1575119640; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242019-12-4%24%u5357%u5B81%28%u5434%u5729%u56FD%u9645%u673A%u573A%29%28NNG%29%24NNG%24%24%24"}; _bfa=1.1573299825075.2c2710.1.1574130278578.1575119584536.9.82; _bfs=1.3; _jzqco=%7C%7C%7C%7C%7C1.51473978.1573299831438.1575119640308.1575119698012.1575119640308.1575119698012.0.0.0.65.65; __zpspc=9.10.1575119640.1575119698.2%233%7Cwww.google.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D100101991%26v1%3D82%26v2%3D81',
    #    'Referer': 'https://www.ctrip.com/',
    #    

    chrome_options.add_argument(headers)
    browser=webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url+city[start]+'-'+city[end]+'?date='+date_time)

    #获取元素位置并填入
    browser.implicitly_wait(random.choice([1,2,3])) 
    try:
        tickets_elements=browser.find_elements_by_class_name('search_table_header')
    except:
        print('获取元素失败')
        return None

    # 爬去元素
    for item in tickets_elements:
        info_dict={}
        info=item.text.split('\n')
        if info[0][0]=='当':
            del info[0]
        if '经停' in info:
            info_dict['起飞星期']=week_day
            info_dict['飞机型号']=info[0]+info[1]
            info_dict['起飞时间']=info[2]+'({})'
            info_dict['起飞机场']=info[3]+'({})'.format(start)
            info_dict['降落时间']=info[6]
            info_dict['降落机场']=info[7]+'({})'.format(end)
            info_dict['准点率']=info[9]
            info_dict['价格']=int(re.findall(r'\d+\.?\d*',info[10])[0])
            info_dict['直达状况']='直达'
            info_list.append(info_dict)
        else:
            info_dict['起飞星期']=week_day
            info_dict['飞机型号']=info[0]+info[1]
            info_dict['起飞时间']=info[2]
            info_dict['起飞机场']=info[3]+'({})'.format(start)
            info_dict['降落时间']=info[4]
            info_dict['降落机场']=info[5]+'({})'.format(end)
            info_dict['准点率']=info[7]
            info_dict['价格']=int(re.findall(r'\d+\.?\d*',info[8])[0])
            info_dict['直达状况']='直达'
            info_list.append(info_dict)
        # print(info)
    browser.close()
    return info_list

    
#获取未来三个月的日期
def getDate(today):
    dates=[]
    begin=today+ datetime.timedelta(days=1)
    end=begin+relativedelta(months=+3)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        dates.append(day)
    return dates


if __name__ == '__main__':
    tosql=Tosql()
    departure=['天津','北京','石家庄'] # 出发地
    destination=['南宁','桂林','梧州','柳州','北海'] # 目的地
    dates=getDate(datetime.date.today()) # 日期
    search_list=[]
    for on in departure:
        for off in destination:
            for date in dates:
                search_list=info_search('https://flights.ctrip.com/itinerary/oneway/',on,off,date)
                print(search_list)
                tosql.insert(search_list)


# # !/usr/bin/env python
# # -*- coding: utf-8 -*-

# import asyncio
# import requests
# import datetime
# import json
# import csv
# import time
# import random
# import re
# #----------module document----------
# __pyVersion__ = '3.6.0'
# __author__ = 'Zhongxin Yue'
# #----------module document----------

# __doc__ = '''                           A Page Scraper for Ctrip.
# 获取携程网单程机票信息 url:'http://flights.ctrip.com/domestic/Search/FirstRoute' 爬取方式：asyncio
# 默认爬取内容：默认爬取厦门到上海2017-4-4至2017-4-6 的机票信息,默认存储方式：csv
# 使用说明：可以在创建实例时依次给入参数
# city1对应出发城市
# city2对应到达城市
# day1对应起始时间
# day2对应最终时间
# 如crawler = Xiecheng(city1='BJS'，city='SHA',day1=(2017,4,4),day2=(2017,4,6)) 爬取北京到上海2017-4-4到2017-4-6的机票信息
# 更多功能进一步讨论后再添加...
# '''

# class Xiecheng(object):
# #默认爬取   XMN SHA day1=(2017, 4, 4)-day2 =(2017, 4, 6)
#     def __init__(self,city1 ='XMN',city2 ='SHA',day1=(2019, 12, 4),day2 =(2019, 12, 6)):
# #爬取单程机票的爬虫 缺少参数依次为（出发城市，到达城市，日期）
#         self.init_url = 'https://flights.ctrip.com/itinerary/oneway/{}-{}?date={}'.format(city1,city2,day1)
# #初始化爬取的参数
#         self.from_city = city1
#         self.to_city = city2
#         self.st_day = day1
#         self.end_day = day2
# #作为存储文件的名字
#         self.save_name = self.from_city + '-'+self.to_city


# #用于返回一个时间list来构造url
#     def datelist(self,start, end):
#         start_date = datetime.date(*start)
#         end_date = datetime.date(*end)

#         result = []
#         curr_date = start_date
#         while curr_date != end_date:
#             result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
#             curr_date += datetime.timedelta(1)
#         result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
#         return result

# #用于构造url的list
#     def join_url(self):
#         '''
#         payload 输入三个参数分别为出发城市，到达城市，出发日期  并构造储存名
#         '''
#         date_list = self.datelist(self.st_day, self.end_day)

#         joinurls = []
#         for i in date_list:
#             joinurls.append(self.init_url.format(DCity1=self.from_city, ACity1= self.to_city, DDate1=i))

#         return joinurls

# #抓取函数
#     def get_html(self,url):
#         USER_AGENT_LIST = [
#             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'

#             'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#             'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#             'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#             'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
#             'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#             'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#             'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
#             'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
#             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',

#         ]

#         user_agent = (random.choice(USER_AGENT_LIST))
#         headers = {'User-Agent': user_agent,
#                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                    'accept-encoding':'gzip, deflate, br',
#                    'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
#                    'cache-control':'max-age=0',
#                    'cookie':'_abtest_userid=427f44ed-cf0b-4c75-b995-b4ca21d572fe; _ga=GA1.2.1406023646.1573299831; _RF1=111.207.1.146; _RSG=7_aiNPEaVwC1J9izn1bcvA; _RDG=28a1df2533a37725e23e1a74ab64575ae6; _RGUID=ce9f90e6-57b2-4fc7-ae66-941c7db094c1; Session=smartlinkcode=U135371&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; appFloatCnt=5; _gid=GA1.2.1669130808.1575119640; MKT_Pagesource=PC; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242019-12-4%24%u5357%u5B81%28%u5434%u5729%u56FD%u9645%u673A%u573A%29%28NNG%29%24NNG%24%24%24"}; _bfa=1.1573299825075.2c2710.1.1574130278578.1575119584536.9.82; _bfs=1.3; _jzqco=%7C%7C%7C%7C%7C1.51473978.1573299831438.1575119640308.1575119698012.1575119640308.1575119698012.0.0.0.65.65; __zpspc=9.10.1575119640.1575119698.2%233%7Cwww.google.com%7C%7C%7C%7C%23; _bfi=p1%3D10320673302%26p2%3D100101991%26v1%3D82%26v2%3D81',
#                    'Referer': 'https://www.ctrip.com/',
#                     }
#         try:
#             r = requests.get(url, headers)
#             print('成功获取',url)
#             return r.content
#         except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
#             print('Fail to get', url)
#             return None
# #解析爬取的html（json格式的信息）

# #解析函数

#     def parse_json(self, html):
#         if html:
#             # print(html)
#             info = json.loads(html)
#             fis = info['fis']
#             info_list = []
#             for i in fis:
#                 slist = []
#                 slist.append(i['fn'])
#                 slist.append(str(i['dcn']))
#                 slist.append(str(i['dpbn']))
#                 slist.append(str(i['acn']))
#                 slist.append(str(i['apbn']))
#                 slist.append(str(i['dt']))
#                 slist.append(str(i['at']))
#                 slist.append(str(i['lp']))

#                 info_list.append(slist)

#             self.save_csv(info_list)
#             print('存储成功')

#         else:
#             print('Fail to get info')

# #将爬取的数据存储为csv格式

# #存储函数

#     def save_csv(self,info_list):
#         with open(self.save_name, 'a', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerows(info_list)

# #构建文件的函数

#     def create_csv(self):
#         titles = ['fn','dpt_city', 'dpt_airport', 'at_city', 'at_airport', 'dpt_time', 'at_time', 'price']
#         with open(self.save_name, 'w',newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(titles)

#     async def running(self,url):
#         html = self.get_html(url)
#         self.parse_json(html)

#     def run(self):
#         self.create_csv()
#         loop = asyncio.get_event_loop()
#         urls = self.join_url()
#         tasks = [self.running(url) for url in urls]
#         loop.run_until_complete(asyncio.wait(tasks))
#         loop.close()
#         with open(self.save_name, 'r') as csvfile:
#             reader = csv.reader(csvfile)
#             rows = [row for row in reader]
#         print('总共抓取：', len(rows)-1,'条')

# if __name__ == '__main__':
#     print(__doc__)
#     st = time.time()

#     crawler = Xiecheng()
#     crawler.run()

#     end = time.time()
#     print('爬取时间',datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
#     print('耗时:',end-st)