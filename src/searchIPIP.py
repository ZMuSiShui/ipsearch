#!/usr/bin/python

import re
import ipdb
from IPy import IPSet

ipy = IPSet()

try:
    ipdbsource = ipdb.City("src/mydata4vipday2.ipdb")
except:
    ipdbsource = ipdb.City("src/mydata4vipday2.ipdb_bak")

def searchFromIPIP(data):
    """
    :param data:
        @country_name : 国家名字
        @region_name  : 省名字
        @city_name    : 城市名字
        @owner_domain : 所有者
        @isp_domain  : 运营商
        @latitude  :  纬度
        @longitude : 经度
        @timezone : 时区
        @utc_offset : UTC时区
        @china_admin_code : 中国行政区划代码
        @idd_code : 国家电话号码前缀
        @country_code : 国家2位代码
    :return:
        ipstr
    """
    ipstr = ""
    for i in data:
        try:
            ip = i.split('/')[0]
            if ip:
                iplist = ipdbsource.find(ip,"CN")
                ipinfo = f"{ip} {iplist[0]} {iplist[1]} {iplist[2]} {iplist[3]} {iplist[4]} {iplist[-6]} {iplist[-2]} {iplist[-1]}".strip()
                ipinfo = re.sub(r"\s+", " ", ipinfo)
                ipstr += ipinfo + "\n"
        except:
            ipstr += "The current parameter is not supported \n"
    return ipstr
if __name__ == "__main__":
    iplist = ["119.28.31.229","1.1.1.1"]
    searchFromIPIP(iplist)




