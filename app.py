# coding: utf-8
import json
import re
import sys
import time
import requests

def send_message(msg):
  api = "https://sc.ftqq.com/SCU149433Tafeec016e8cdd993fd39b02078af4c515ffd5832aa76a.send"
  title = "爱奇艺签到通知"
  data = {
    "text":title,
    "desp":msg
  }
  req = requests.post(api,data = data)

def start():
  cookie='QC180=; QC006=tcq2suuqf61yz4eygicwu0zh; QC173=0; P00004=.1560348030.b99d47e6ca; __uuid=11bc7ab2-8357-4e1c-056a-ecf1b4325dd8; QP001=1; QP0017=100; QP0018=100; QC124=1%7C0; _ga=GA1.2.2046446051.1560583836; QC005=4c268614a10616ab6a230e8f3ee33ded; T00404=92fd082cf86964a48a6a7f4ed6e3b2bc; QC118=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A0%7D; cuuid=22e95b20e489426d810e3daa42871f58; QC170.sig=5QY_l_EMGEFy9_9zKtnZraEUga4; QP0028=1; QP007=0; QP0030=1; QIYUECK=qy_pc_c41a0946736946c0a9c6ffb4537a2268; QP0013=0; 4c268614a10616ab6a230e8f3ee33ded=1569057557.1592020360.1608456763.3; QCUser=true; QC021=%5B%7B%22key%22%3A%22%E8%B5%A4%E7%8B%90%E4%B9%A6%E7%94%9F%22%7D%2C%7B%22key%22%3A%22%E6%A2%A6%E6%83%B3%E6%94%B9%E9%80%A0%E5%AE%B6%E7%AC%AC7%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E6%A2%A6%E6%83%B3%E6%94%B9%E9%80%A0%E5%AE%B6%E7%AC%AC5%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E4%BF%A1%E6%9D%A1%22%7D%2C%7B%22key%22%3A%22%E6%A2%A6%E6%83%B3%E6%94%B9%E9%80%A0%E5%AE%B6%E7%AC%AC6%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E6%A2%A6%E6%83%B3%E6%94%B9%E9%80%A0%E5%AE%B6%E7%AC%AC4%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E8%B4%A2%E7%BB%8F%E9%83%8E%E7%9C%BC2020%E5%B9%B4%22%7D%2C%7B%22key%22%3A%22%E6%A2%A6%E6%83%B3%E6%94%B9%E9%80%A0%E5%AE%B6%E7%AC%AC3%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E6%A2%A6%E6%83%B3%E6%94%B9%E9%80%A0%E5%AE%B6%E7%AC%AC2%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E4%BD%BF%E5%BE%92%E8%A1%8C%E8%80%85%E4%B9%8B3%22%7D%5D; IMS=IggQARj_gaj_BSokCiBjZmNiM2QzZjZhMzZkNDA2M2I4YzgwYmFiODcwNDY3MRAAciQKIGNmY2IzZDNmNmEzNmQ0MDYzYjhjODBiYWI4NzA0NjcxEACCAQCKASQKIgogY2ZjYjNkM2Y2YTM2ZDQwNjNiOGM4MGJhYjg3MDQ2NzE; QC007=DIRECT; QC008=1560347992.1608203111.1610363935.32; nu=0; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1608094019,1608206724,1610363940; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1610363940; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A0%2C%22hadTip%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A30%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22isset%22%3A1%2C%22hideRoleTip%22%3A1%2C%22isFilterHongbao%22%3A0%7D; QP008=1140; QC175={%22upd%22:true%2C%22ct%22:1610874526398}; QY_PUSHMSG_ID=4c268614a10616ab6a230e8f3ee33ded; QP0022=CMNET%7CFuJian_FuZhou-112.49.84.85%7Cbaiducdn2_cmnet; P00001=eaASHAElzZqtaWkn6fXpucz2M8itTsNEoS8dm1em3chWtyB21wxHZTXZRYWbCzEJm1UG48f; P00007=eaASHAElzZqtaWkn6fXpucz2M8itTsNEoS8dm1em3chWtyB21wxHZTXZRYWbCzEJm1UG48f; P00003=1469668262; P00002=%7B%22uid%22%3A1469668262%2C%22pru%22%3A1469668262%2C%22user_name%22%3A%2217606072430%22%2C%22nickname%22%3A%22%5Cu559c%5Cu6b22%5Cu61d2%5Cu5e8a%5Cu7684%5Cu5b50%5Cu6851%5Cu548c%5Cu6d3d%22%2C%22pnickname%22%3A%22%5Cu559c%5Cu6b22%5Cu61d2%5Cu5e8a%5Cu7684%5Cu5b50%5Cu6851%5Cu548c%5Cu6d3d%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D; P00010=1469668262; P01010=1612022400; P00PRU=1469668262; QC170=1; QC163=1; QC179=%7B%22vipTypes%22%3A%221%22%2C%22userIcon%22%3A%22%2F%2Fwww.iqiyipic.com%2Fcommon%2Ffix%2Fheadicons%2Ffemale-130.png%22%2C%22iconPendant%22%3A%22%22%2C%22uid%22%3A1469668262%7D; __dfp=a1aa36bc5ce8604b9ba6a7e5ed1aa1381907b88fdd33a471ce49b98b2965391917@1613268184865@1611972185865; QC010=258279822'
  regex1=re.compile("P00001=(.*?);")
  P00001=regex1.findall(cookie)
  headers = {
    'Cookie':cookie,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  }
  login = requests.get('https://static.iqiyi.com/js/qiyiV2/20200212173428/common/common.js',headers=headers).text
  regex1=re.compile("platform:\"(.*?)\"")
  platform=regex1.findall(login)
  url='https://tc.vip.iqiyi.com/taskCenter/task/userSign?P00001='+P00001[0]+'&platform='+platform[0] + '&lang=zh_CN&app_lm=cn&deviceID=pcw-pc&version=v2'
  sign=requests.get(url, headers=headers).text
  send_message(sign)

  str=json.loads(sign)
  str=str["data"]["acquireGiftList"][0]

def main_handler():
  while True:
    now_hour = time.strftime("%H", time.localtime())
    now_min = time.strftime("%M", time.localtime())
    if now_hour < "08":
        rest = 8 - int(now_hour)
        sleeptime = (rest-1)*3600 + (60-int(now_min))*60
        print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t软件将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour > "08":
        rest = 8 - int(now_hour) + 24
        sleeptime = (rest-1)*3600 + (60-int(now_min))*60
        print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t软件将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour == "08":
        print("启动时北京时间为：" + time.strftime("%H:%M", time.localtime()), "\t软件将在每天8点发送数据！")
        # 以下为定时任务，定时执行签到任务
        start()
        print("数据")
        time.sleep(86400-int(now_min)*60)

if __name__ == '__main__':
  main_handler()