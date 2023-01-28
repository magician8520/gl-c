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
        print(state.json())
        time = state.json()['data']['leftDays']
        days = time.split('.')[0]
        print(mess)
        print('剩余天数：' + days + '天')

    checkin.close()
    state.close()

    return checkin.status_code, state.status_code, mess, days


def sign(cookie, pathd):
    date_time = str(datetime.now())[:7]
    # try:
    checkin_status_code, state_status_code, mess, days = start(cookie)
    #     date_log = f'{str(datetime.now())[:19]}: checkin({checkin_status_code}); state({state_status_code}) \n    {mess} \n    剩余天数：{days}\n'
    #     with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
    #         f.write(date_log)

    # except Exception as e:
    #     err_log = f'{datetime.now().date()}: {e}\n'
    #     with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
    #         f.write(err_log)
            
    # finally:
    #     with open(f'{pathd}/Clash_log/Clash_{date_time}.log', 'a') as f:
    #         f.write('---===---===---===---===---===---===---\n')

def main():
    pathd = paths[0].replace('\\', '/')

    # cookies = get_cks(pathd)
    # if not cookies:
        # return
    print(argv)
    for ck in argv[1:]:
        # cookie = cookies.get(ck)
        print(ck)
        sign(ck, pathd)
   
    # input('任意键结束：')

if __name__ == '__main__':
    main()
