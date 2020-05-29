import time
import os
import sys
from hashlib import md5
from urllib import parse
from urllib import request

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from config.settings import API, APPID, SECRETKEY


def create_nic(sor_data):
    """
    更新网卡数据
    sor:{'status': 1, 'data': {'eth0': {'up': True, 'hwaddr': '00:1c:42:a5:57:7a', 'ipaddrs': '10.211.55.4', 'netmask': '255.255.255.0'}}}
    target:
    """
    myurl = API + '/nic/'
    for nic_name, nic_value in sor_data['data'].items():
        # 字典合并
        # dict( dict1.items() + dict2.items() )
        # dict( dict1, **dict2 )
        # dictMerged3 = dict1.copy();dictMerged3.update( dict2 )
        nic_value.update({"name": nic_name, "server_obj": '1'})
        data = nic_value
    timestamp = str(int(time.time()))
    sign = APPID + SECRETKEY + timestamp
    m1 = md5()
    m1.update(sign.encode(encoding='utf8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + APPID + '&sign=' + sign + '&timestamp=' + timestamp
    print(myurl)
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
    }

    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(myurl, headers=headers, data=data)  # POST方法
    # req = request.Request(url+params)  # GET方法
    page = request.urlopen(req).read()
    # page = page.decode('utf-8')
    print(page)
