#### cookie获取方式
1.打开https://www.iqiyi.com/并登录
2.f12翻到第一个https://www.iqiyi.com/ 双击复制request headers 里面的cookie

##### 部署方式
1. 安装：pip3 install -r requirements.txt
2. 创建screen：screen -S sign_iqiyi
3. 启动服务：python ./app.py
4. 退出：^ A D

screen -ls         -> 列出当前所有的session
screen -r yourname -> 回到yourname这个session
