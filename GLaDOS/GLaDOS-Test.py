#!/usr/bin/python

from os import path, mkdir
from sys import path as paths, argv
from json import dumps as jdumps
from yaml import load as yload, Loader as yLoader
from requests import post, get
from datetime import datetime

def start(cookie):
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    # checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    # state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 " \
                "Safari/537.36 "
    payload = {
        # 'token': 'glados_network'
        'token': 'glados.network'
    }
    checkin = post(
        url,
        headers={'cookie': cookie, 'referer': referer, 'origin': origin, 
        'user-agent': useragent,
        'content-type': 'application/json;charset=UTF-8'}, 
        data=jdumps(payload)
    )
    state = get(url2,
        headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
    # print(checkin.text)
    # print(state.text)
    print(checkin.status_code)
    print(state.status_code)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        days = time.split('.')[0]
        print(mess)
        print('剩余天数：' + days + '天')

    checkin.close()
    state.close()

    return checkin.status_code, state.status_code, mess, days

def get_cks(pathd, date_time):
    try:
        # 检查日志文件夹
        if not path.exists(f'{pathd}/Clash_log'):
            print('检测到没有日志文件夹，正则创建...')
            mkdir(f'{pathd}/Clash_log')
            print('日志文件夹创建成功！')

        # 检查cookies配置
        if not path.exists(f'{pathd}/cookies.yaml'):
            print('检测到没有cookie.yaml文件，正在创建...\n')
            file = open(f'{pathd}/cookies.yaml', 'w', encoding='utf-8')
            file.write("# 一行一个cookie\n# 格式：\n# '账号': 'cookie'\n")
            file.close()
            print('cookies.yaml创建成功! \n')
            print('你没有配置cookie，请将你的cookie按格式填入cookies.yaml文件中\n')
            print('然后重新运行脚本')
            return False

        with open(f'{pathd}/cookies.yaml', 'r', encoding='utf-8') as fr:
            cookies = yload(fr, yLoader)

        if type(cookies) != dict:
            print('请先配置cookie！！！')
            return False

        return cookies

    except Exception as e:
        err_log = f'{datetime.now().date()}: {e}\n'
        with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
            f.write(err_log)
            
    finally:
        with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
            f.write('---===---===---===---===---===---===---\n')
        return False
        

def sign(cookie, pathd, date_time):
    
    try:
        checkin_status_code, state_status_code, mess, days = start(cookie)
        date_log = f'{str(datetime.now())[:19]}: checkin({checkin_status_code}); state({state_status_code}) \n    {mess} \n    剩余天数：{days}\n'
        with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
            f.write(date_log)

    except Exception as e:
        err_log = f'{datetime.now().date()}: {e}\n'
        with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
            f.write(err_log)
            
    finally:
        with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
            f.write('---===---===---===---===---===---===---\n')
        

def main():

    pathd = paths[0].replace('\\', '/')
    date_time = str(datetime.now())[:7]
    # cookies = get_cks(pathd, date_time)
    cookies = argv[1:]
    if not cookies:
        return
    
    for ck in cookies:
        print(ck)
        sign(ck, pathd, date_time)
   
    input('任意键结束：')

if __name__ == '__main__':
    main()
