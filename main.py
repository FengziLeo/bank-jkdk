import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json

# 创建 SMTP 对象
smtp = smtplib.SMTP()
# 连接（connect）指定服务器
smtp.connect("smtp.qq.com", port=587)
# 登录，需要：登录邮箱和授权码
smtp.login(user="sample@qq.com", password="Your email passwd")


url = 'https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak'

header = {
    'Host': 'app.xiaoyuan.ccb.com',
    'Content-Type':'application/json;charset=UTF-8',
    'Origin': 'https://app.xiaoyuan.ccb.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'cokie',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 jianronghuixue/1.3.4',
    'Referer': 'https://app.xiaoyuan.ccb.com/EMTSTATIC/DZK2022111901/index2022111901.html',
    'Content-Length': '1184',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
    }

data = {
  "isContactWithDiagnosis" : "N",
  "locationAddr" : "Your location",
  "remarks" : 'null',
  "id" : "Your id",
  "noseStartTime" : "",
  "isLevel" : "N",
  "arriveAddr" : "",
  "nowStatusStartTime" : "",
  "stuClass" : "9999",
  "familyaddress" : "***",
  "headacheStartTime" : "",
  "professional" : "",
  "dateOfDisengagement" : "",
  "fatigueStartTime" : "",
  "throatStartTime" : "",
  "familyStatus" : "0",
  "injectTimes" : "3",
  "runnyStartTime" : "",
  "isInSchool" : "",
  "backtime" : "",
  "otherDesc" : 'null',
  "userId" : "***",
  "feverStartTime" : "",
  "nowStatus" : "0",
  "healthStatus" : "3",
  "personCategory" : 'null',
  "coldStartTime" : "",
  "familyStatusStartTime" : "",
  "departments" : "",
  "isFever" : "0",
  "diagnosisTreatment" : "",
  "backTrafficNo" : "",
  "backTrafficTool" : "",
  "isContact" : "N",
  "levelDate" : "",
  "isbackLive" : "N",
  "otherSymptoms" : "",
  "personType" : "",
  "isVaccinate" : "1",
  "vaccineType" : "2",
  "trafficTool" : "",
  "stName" : "**",
  "temperature" : 36.299999999999997,
  "isWuhan" : "N",
  "schoolId" : "**",
  "conjunctivaStartTime" : "",
  "timeToLeaveHuBei" : "",
  "isAppearDiagnosis" : "N",
  "schoolName" : "**",
  "trafficNo" : "",
  "diarrheaStartTime" : "",
  "stId" : "**",
  "coughStartTime" : "",
  "stMobile" : "1**",
  "nowArea" : "**"
}

res = requests.post(url,json=data,headers=header)

res1 = str(res.json())
if '提交成功，谢谢您' in res1:
    res1 = '已成功'
#print(res.text)

message = MIMEText(res.text, 'plain', 'utf-8')
message['From'] = Header("今日打卡", 'utf-8')  # 发件人的昵称
message['To'] = Header('健康打卡', 'utf-8')  # 收件人的昵称
message['Subject'] = Header(res1, 'utf-8')  # 定义主题内容
#print(message)

smtp.sendmail(from_addr="sample@qq.com", to_addrs="sample@qq.com", msg=message.as_string())
