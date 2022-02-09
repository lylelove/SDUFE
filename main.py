import requests
import io
import json
import base64

import ddddocr
import os
import sys


def getImg(cookies):
    imagetest = requests.get('http://bcfl.sdufe.edu.cn/index.php?g=api&m=checkcode&a=index', cookies=cookies)
    imagebody = imagetest.content
    file_name = 'index.png'
    with open(file_name, "wb") as f:
        f.write(imagebody)


def getverify():
    try:
        ocr = ddddocr.DdddOcr()
        with open("index.png", 'rb') as f:
            img_bytes = f.read()
        verify = ocr.classification(img_bytes)
    except:
        verify = 0000
    return verify


def getcookie(headers):
    '''
    获取Cookie
    '''
    url = 'http://bcfl.sdufe.edu.cn/index/login'
    with requests.Session() as s:
        r = s.post(url, headers=headers)
        cookies = {'PHPSESSID': requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']}
    return cookies


def login(cookies, headers, number, card):
    '''
    进行登录
    '''
    loopcount = 0
    logincode = 201
    loginurl = 'http://bcfl.sdufe.edu.cn/Student/handle_login'
    while logincode == 201:
        try:
            getImg(cookies)
            verify = getverify()
            print(verify)
            data = 'number={}&card={}&verify={}'.format(number, card, verify)
            response = requests.post(url=loginurl, headers=headers, data=data, cookies=cookies)
            logincode = response.json()['code']
        except:
            logincode = 201
        loopcount += 1
        print('{} is {}'.format(loopcount, logincode))

    print('finish login...')


def register(cookies, headers, basicinfo):
    '''
    进行打卡操作
    '''
    loopcount = 0
    registercode = 201
    registerurl = 'http://bcfl.sdufe.edu.cn/Student/handle_ext_do'
    while registercode == 201:
        try:
            getImg(cookies)
            verify = getverify()
            print(verify)
            info = basicinfo + 'verify={}'.format(verify)
            response = requests.get(url=registerurl, headers=headers, data=info, cookies=cookies)
            registercode = response.json()['code']
        except:
            verifycode = 201
        loopcount += 1
        print('{} is {}'.format(loopcount, registercode))

    print('finish register!')


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
           'Referer': 'http://bcfl.sdufe.edu.cn/index/login.html',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Host': 'bcfl.sdufe.edu.cn',
           'Accept': '*/*'}

number = eval(sys.argv[1])
card = sys.argv[2]
basicinfo = sys.argv[3]

cookies = getcookie(headers)
login(cookies, headers, number, card)
register(cookies, headers, basicinfo)

exit()
