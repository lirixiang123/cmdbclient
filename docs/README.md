[TOC]



#### 1. 数据收集

* 安装系统时部署此agent，并加入crontab，小时执行一次数据收集与校验
* 检查此agent是否部署在crontab中，并作为zabbix的监控项



#### 2. 目录说明

```
.
├── bin                     // 运行脚本目录 
│   ├── run.py 
│   └── servers_info.py
├── config                 // 配置目录
│   └── settings.py
├── docs
│   ├── README.md
│   ├── windows平台获取信息指令.txt
│   ├── 使用方法.txt
│   └── 代码规范.txt
├── files                   // Linux下获取数据的格式 
├── lib                
│   ├── apimethod.py
│   ├── convert.py
│   ├── log.py
│   └── response.py
├── log                    // 日志目录
├── plugins                // 获取数据的脚本
│   ├── BasePlugin.py
│   ├── CpuPlugin.py
│   ├── DiskPlugin.py
│   ├── MemoryPlugin.py
│   ├── MotherboardPlugin.py
│   ├── NicPlugin.py
│   ├── PluginApi.py
└── requirements.txt      // 所有依赖包
```



#### 3.收集的数据

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |



#### 4. 收集脚本

* 脚本功能

  * 运行脚本，将会收集服务器信息
  * 收集到的信息会发送到对应的api接口
  
* 调用方式()

  * 手动调用

    ```
    cd cmdbclient
    python bin/run.py
    ```

  * crontab

    ```
    # crontab -e
    0 1 * * * cd cmdbclient; /usr/bin/python bin/run.py >/dev/null 2>&1 
    ```

    

* 数据格式

  > json格式化展示工具：http://www.bejson.com/
  
  ```
  {
  	"status": true,
  	"message": "",
  	"data": {
  		"os_platform": "Linux",
  		"os_version": "CentOS Linux 7 Core",
  		"manufactory": "VMware, Inc.",
  		"model": "VMware Virtual Platform",
  		"sn": "VMware-56 4d ee 10 1e 66 d7 db-4c 60 ab 72 71 f5 f2 94",
  		"cpu_count": 4,
  		"cpu_physical_count": 2,
  		"cpu_model": " Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz",
  		"disk": {
  			"status": 1,
  			"data": {
  				"0": {
  					"slot": "0",
  					"capacity": "279.396",
  					"model": "SEAGATE ST300MM0006     LS08S0K2B5NV",
  					"pd_type": "SAS"
  				},
  				"1": {
  					"slot": "1",
  					"capacity": "476.939",
  					"model": "S1SZNSAFA01085L Samsung SSD 850 PRO 512GB               EXM01B6Q",
  					"pd_type": "SATA"
  				}
  			}
  		},
  		"memory": {
  			"status": 1,
  			"data": {
  				"RAM slot #0": {
  					"capacity": 1024,
  					"slot": "RAM slot #0",
  					"model": "DRAM",
  					"speed": "Unknown",
  					"manufactory": "Not Specified",
  					"sn": "Not Specified"
  				}
  			}
  		},
  		"nic": {
  			"status": 1,
  			"data": {
  				"ens33": {
  					"up": true,
  					"hwaddr": "00:0c:29:f5:f2:94",
  					"ipaddrs": "192.168.189.100",
  					"netmask": "255.255.255.0"
  				},
  				"docker0": {
  					"up": true,
  					"hwaddr": "02:42:25:77:93:ac",
  					"ipaddrs": "172.17.0.1",
  					"netmask": "255.255.0.0"
  				},
  				"br-938880f7bcd1": {
  					"up": true,
  					"hwaddr": "02:42:1c:1e:5a:e7",
  					"ipaddrs": "172.18.0.1",
  					"netmask": "255.255.0.0"
  				}
  			}
  		}
  	}
  }
  ```



#### 5. 代码规划

