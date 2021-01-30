# coding: utf-8
import json
import re
import sys
import time

import requests

Push_Key = '请填写key'
Cookie='请填写cookie'

def send_message(msg):
  api = "https://sc.ftqq.com/" + Push_Key + ".send"
  title = "爱奇艺签到通知"
  data = {
    "text":title,
    "desp":msg
  }
  req = requests.post(api,data = data)

def start():
  regex1=re.compile("P00001=(.*?);")
  P00001=regex1.findall(Cookie)
  headers = {
    'Cookie':Cookie,
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
    if now_hour < "12":
        rest = 8 - int(now_hour)
        sleeptime = (rest-1)*3600 + (60-int(now_min))*60
        print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t软件将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour > "12":
        rest = 8 - int(now_hour) + 24
        sleeptime = (rest-1)*3600 + (60-int(now_min))*60
        print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t软件将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour == "12":
        print("启动时北京时间为：" + time.strftime("%H:%M", time.localtime()), "\t软件将在每天8点发送数据！")
        # 以下为定时任务，定时执行签到任务
        start()
        print("数据")
        time.sleep(86400-int(now_min)*60)

if __name__ == '__main__':
  main_handler()