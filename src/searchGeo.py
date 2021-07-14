import geoip2.database
import re

def searchFromMaxmind(data):
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
    with geoip2.database.Reader("src/GeoIP2-City.mmdb") as reader:
        ipstr = ""
        for i in data:
            try:
                ip = i.split('/')[0]
                if ip:
                    response = reader.city(ip)
                    country_name = response.country.names['zh-CN']
                    try:
                        city_name = response.city.names['zh-CN']
                    except:
                        city_name = response.city.name
                    timezone = response.location.time_zone
                    ipinfo = f"{ip} {country_name} {city_name} {timezone}".replace("None","").strip()
                    ipinfo = re.sub(r"\s+", " ", ipinfo)
                    ipstr += ipinfo + "\n"
            except:
                ipstr += "The current parameter is not supported \n"
        return ipstr

if __name__ == "__main__":
    print(searchFromMaxmind(["8.8.8.8"]))