# bank-jkdk
## 代码实现内容
通过定时程序运行，向指定网址提交表单，通过网页反馈的信息来判断是否打卡成功。打卡成功后通过邮件发送告知，可以通过邮件的内容来进行判断

理论上适用于所有建行所搭建的健康打卡程序
某停水停电大学可以正常使用

需要安装requests库以及json库
代码当中的header以及data都需要自己进行抓包
data抓包后需要将数值全部打上双引号或单引号，改为字符串类型

## 注意
政策逐渐放开，但不代表可以完全置之身后，本代码仅供交流学习，切记：健康打卡是对自己负责