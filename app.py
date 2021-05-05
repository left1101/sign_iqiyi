# coding: utf-8
import json
import re
import sys
import time

import requests

Push_Key = 'SCU149433Tafeec016e8cdd993fd39b02078af4c515ffd5832aa76a'
Cookie='QC006=tcq2suuqf61yz4eygicwu0zh; P00004=.1560348030.b99d47e6ca; QP001=1; QP0017=100; QP0018=100; QC124=1%7C0; _ga=GA1.2.2046446051.1560583836; T00404=92fd082cf86964a48a6a7f4ed6e3b2bc; cuuid=22e95b20e489426d810e3daa42871f58; QC170.sig=5QY_l_EMGEFy9_9zKtnZraEUga4; QP0028=1; QP007=0; QP0030=1; QIYUECK=qy_pc_c41a0946736946c0a9c6ffb4537a2268; QC005=23062f61069dbb8b7162f802bc9d871a; QC173=0; P00003=1469668262; P00002=%7B%22uid%22%3A1469668262%2C%22pru%22%3A1469668262%2C%22user_name%22%3A%2217606072430%22%2C%22nickname%22%3A%22%5Cu559c%5Cu6b22%5Cu61d2%5Cu5e8a%5Cu7684%5Cu5b50%5Cu6851%5Cu548c%5Cu6d3d%22%2C%22pnickname%22%3A%22%5Cu559c%5Cu6b22%5Cu61d2%5Cu5e8a%5Cu7684%5Cu5b50%5Cu6851%5Cu548c%5Cu6d3d%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D; P00010=1469668262; P01010=1616860800; P00PRU=1469668262; QC170=1; QC007=DIRECT; QC008=1560347992.1615113111.1619847024.35; QP0013=1; nu=0; P00001=17E7rGPxlgAtiiSklbeYNfUv6a0xPQ0A4TRIv6dyxUtuWaAPCA8m3WQkrGyVw2b1bN3d6; P00007=17E7rGPxlgAtiiSklbeYNfUv6a0xPQ0A4TRIv6dyxUtuWaAPCA8m3WQkrGyVw2b1bN3d6; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1619847063; QC021=%5B%7B%22key%22%3A%22%E5%94%90%E4%BA%BA%E8%A1%97%E6%8E%A2%E6%A1%883%22%7D%2C%7B%22key%22%3A%22%E5%BA%86%E4%BD%99%E5%B9%B4%E7%AC%AC2%E5%AD%A3%E9%A2%84%E5%91%8A%E7%9F%AD%E8%A7%86%E9%A2%91%22%7D%2C%7B%22key%22%3A%22%E5%BA%86%E4%BD%99%E5%B9%B4%E7%AC%AC2%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E9%87%8D%E5%90%AF%22%7D%2C%7B%22key%22%3A%22%E7%9B%97%E5%A2%93%E7%AC%94%E8%AE%B0%22%7D%2C%7B%22key%22%3A%22%E8%B5%8C%E7%A5%9E3%22%7D%2C%7B%22key%22%3A%22%E8%B5%98%E5%A9%BF%22%7D%2C%7B%22key%22%3A%22%E6%97%8B%E9%A3%8E%E5%B0%8F%E5%AD%90%22%7D%2C%7B%22key%22%3A%22%E6%A8%B1%E6%A1%83%E5%B0%8F%E4%B8%B8%E5%AD%90%E7%AC%AC1%E5%AD%A3%22%7D%2C%7B%22key%22%3A%22%E6%A8%B1%E6%A1%83%E5%B0%8F%E4%B8%B8%E5%AD%90%E7%AC%AC5%E5%AD%A3%22%7D%5D; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1619847201; QP0027=2; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22hadTip%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A30%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22isset%22%3A1%2C%22hideRoleTip%22%3A1%2C%22isFilterHongbao%22%3A0%7D; QP008=900; TQC002=type%3Djspfmc140109%26pla%3D11%26uid%3D23062f61069dbb8b7162f802bc9d871a%26ppuid%3D1469668262%26brs%3DCHROME%26pgtype%3Dplay%26purl%3Dhttps%3A%252F%252Fwww.iqiyi.com%252Fv_19rrcuh1jw.html%26cid%3D1%26tmplt%3D%26tm1%3D6026%2C0%26tm6%3D7524%2C0; QC142=pu_a87c6801f9733765; QC179=%7B%22vipTypes%22%3A%221%22%2C%22userIcon%22%3A%22%2F%2Fwww.iqiyipic.com%2Fcommon%2Ffix%2Fheadicons%2Ffemale-130.png%22%2C%22iconPendant%22%3A%22%22%2C%22uid%22%3A1469668262%7D; QC010=34801829; IMS=IggQABj_gcuEBiomCiBmNzkxNjkxNGJiOTJkMDFlYjhmNjNmYTYxYWQxY2YzZBAAIgByJAogZjc5MTY5MTRiYjkyZDAxZWI4ZjYzZmE2MWFkMWNmM2QQAIIBAIoBJAoiCiBmNzkxNjkxNGJiOTJkMDFlYjhmNjNmYTYxYWQxY2YzZA; QC163=1; QY_PUSHMSG_ID=23062f61069dbb8b7162f802bc9d871a; QC175={%22upd%22:true%2C%22ct%22:1620212621431}; __dfp=a14d394e8d6771418b82082641c20c7cae0991085b111f3683f7caa4e2d0389e1f@1621143024182@1619847025182'
Time_Hour = "08"

def send_message(title, msg):
  api = "https://sc.ftqq.com/" + Push_Key + ".send"
  # title = "爱奇艺签到通知"
  data = {
    "text":title,
    "desp":msg
  }
  req = requests.post(api,data = data)

def sign_txsp():
  cookie1 = 'pgv_pvi=9353552896; RK=qa7YO9J9Yp; ptcz=80abfef4de76da1385a3d90662b89b5b3645d5ed3116c63dd17ace386a29c53a; pgv_pvid=5292434730; tvfe_boss_uuid=77711f62bc4474ff; o_cookie=1004212394; ts_uid=1343044272; tvfe_search_uid=21236dd0-6a89-4b17-a3af-6624baa83ccb; login_remember=qq; pac_uid=1_1004212394; _mta_closed_sysmsg=/--20180926/--20190816; aics=H81xkjyviwG9v7VAqh89NniMWcVRWSe1Cse6ElNl; qb_guid=8198cf1a402d4030ad8ed6e4790a8566; Q-H5-GUID=8198cf1a402d4030ad8ed6e4790a8566; NetType=; iip=0; ts_refer=so.iqiyi.com/; video_guid=77c5941c383a0f76; video_platform=2; pgv_info=ssid=s7875822100; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; ptui_loginuin=1004212394; bucket_id=9231001; txv_boss_uuid=4c57ff9f-7047-5320-47f4-669a55ce582a; uid=410393917; ts_last=v.qq.com/; ptag=|é¡¶éƒ¨å¯¼èˆªåŒº:å¤´åƒæµ®å±‚:ç«‹å³ç™»å½•; main_login=qq; vqq_vuserid=1706473958; vqq_vusession=0RjMas8CcFf8aj1Eq_jyug..; vqq_access_token=BF6CB3F9D6DE3BEC1A6C352CDFCCE1F0; vqq_openid=CEF1867E93F4583837596DAD7A54416F; vqq_appid=101483052; qq_nick=left; qq_head=http://thirdqq.qlogo.cn/g?b=oidb&k=RRkyoZ1RHPlQsoKsich7ia4w&s=640&t=1556485691; lw_nick=left|0|http://thirdqq.qlogo.cn/g?b=oidb&k=RRkyoZ1RHPlQsoKsich7ia4w&s=640&t=1556485691|0; ad_play_index=14; qv_als=y4p2cRriJcEN5eMmA116132797318KiRFg=='
  this_time = int(round(time.time() * 1000))
  login_url = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=' + str(this_time)
  headers={
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36',
      'Cookie': cookie1
  }
  res = requests.get(login_url,headers=headers).text
  print('访问结果：'+res)
  if 'Account Verify Error' in res:
      print('cookies失效，通知SERVER酱！')
      send_message('腾讯视频签到失败', res)
  else:
      print('签到完成')
      send_message('腾讯视频签到成功', res)

def sign_iqiyi():
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
  send_message("爱奇艺签到通知", sign)

  draw_iqiyi(P00001, headers, "爱奇艺抽奖通知1")
  draw_iqiyi(P00001, headers, "爱奇艺抽奖通知2")
  draw_iqiyi(P00001, headers, "爱奇艺抽奖通知3")

  # str=json.loads(sign)
  # str=str["data"]["acquireGiftList"][0]

def draw_iqiyi(cookie, headers, title):
  url = 'https://iface2.iqiyi.com/aggregate/3.0/lottery_activity?app_k=0&app_v=0&platform_id=0&dev_os=0&dev_ua=0&net_sts=0&qyid=0&psp_uid=0&psp_cki=' + cookie[0] + '&psp_status=0&secure_p=0&secure_v=0&req_sn=0'
  draw = requests.get(url, headers=headers).text
  send_message(title, draw)

def main_handler():
  while True:
    now_hour = time.strftime("%H", time.localtime())
    now_min = time.strftime("%M", time.localtime())
    if now_hour < Time_Hour:
        rest = 8 - int(now_hour)
        sleeptime = (rest-1)*3600 + (60-int(now_min))*60
        print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t软件将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour > Time_Hour:
        rest = 8 - int(now_hour) + 24
        sleeptime = (rest-1)*3600 + (60-int(now_min))*60
        print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t软件将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后发送数据")
        time.sleep(sleeptime)
    elif now_hour == Time_Hour:
        print("启动时北京时间为：" + time.strftime("%H:%M", time.localtime()), "\t软件将在每天8点发送数据！")
        # 以下为定时任务，定时执行签到任务
        sign_iqiyi()
        # sign_txsp()
        print("数据")
        time.sleep(86400-int(now_min)*60)

if __name__ == '__main__':
  main_handler()