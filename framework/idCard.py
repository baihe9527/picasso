#-*- coding:utf-8 -*-
'''

Created on 2018年9月7日

@author: 

'''

import random, datetime

from framework.data import ADDR  # 地址码
'''
排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码:
1、地址码 
表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。
2、出生日期码 
表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。 
3、顺序码 
表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。 
4、校验码计算步骤
(1)十七位数字本体码加权求和公式 
S = Sum(Ai * Wi), i = 0, ... , 16 ，先对前17位数字的权求和 
Ai:表示第i位置上的身份证号码数字值(0~9) 
Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
(2)计算模 
Y = mod(S, 11)
(3)根据模，查找得到对应的校验码 
Y: 0 1 2 3 4 5 6 7 8 9 10 
校验码: 1 0 X 9 8 7 6 5 4 3 2
'''
# 随机生成手机号码
def createPhone():
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
           "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def getValidateCheckout(id17):
    '''获得校验码算法'''
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 十七位数字本体码权重
    validate = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']  # mod11,对应校验码字符值
    
    sum = 0
    mode = 0
    for i in range(0, len(id17)):
        sum = sum + int(id17[i]) * weight[i]
    
    mode = sum % 11
    return validate[mode]

def getRandomIdNumber(sex=1):
    '''产生随机可用身份证号，sex = 1表示男性，sex = 0表示女性'''
    # 地址码产生
    addrInfo = random.randint(0, len(ADDR))  # 随机选择一个值
    addrId = ADDR[addrInfo][0]
    addrName = ADDR[addrInfo][1]
    idNumber = str(addrId)
    # 出生日期码
    start, end = "1960-01-01", "2000-12-30"  # 生日起止日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthDays = datetime.datetime.strftime(
    datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d")
    idNumber = idNumber + str(birthDays)
    # 顺序码
    for i in range(2):  # 产生前面的随机值
        n = random.randint(0, 9)  # 最后一个值可以包括
        idNumber = idNumber + str(n)
        
    # 性别数字码
    sexId = random.randrange(sex, 10, step=2)  # 性别码
    idNumber = idNumber + str(sexId)
    # 校验码
    checkOut = getValidateCheckout(idNumber)
    idNumber = idNumber + str(checkOut)
    return idNumber, addrName, addrId, birthDays, sex, checkOut


def getInfoFromId(id18):
    '''从身份证号码中得出个人信息：地址、生日、性别'''
    addrId = id18[0:6]
    for it in ADDR:
        if addrId == str(it[0]):  # 校验码
            addrName = it[1]
            break
        else:  # 未被break终止
            addrName = 'unknown'
    
    birthDays = datetime.datetime.strftime(datetime.datetime.strptime(id18[6:14], "%Y%m%d"), "%Y-%m-%d")
    sex = 'man' if int(id18[-2]) % 2 else 'woman'  # 0为女性，1为男性
    
    return addrName, birthDays, sex
    

def test():
    # print getValidateCheckout("11111111111111111")#该身份证校验码：0
    #print (getRandomIdNumber(0))
    #cid=getRandomIdNumber(1)[0]
    print (getRandomIdNumber(1))

    #print (getInfoFromId('418928198807286045'))
    print (createPhone())

test()
    