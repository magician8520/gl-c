#!/usr/bin/python

from os import path,environ
from sys import path as paths
from requests import post, get

def start(cookie):
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 " \
                "Safari/537.36 "
    payload = {
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


def sign(cookie, pathd):
    checkin_status_code, state_status_code, mess, days = start(cookie)

def main():
    pathd = paths[0].replace('\\', '/')
    ck = environ["cookie"]
    sign(ck, pathd)

if __name__ == '__main__':
    main()
