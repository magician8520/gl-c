from os import environ
from Check import CheckIn
from push import send_msg

if __name__ == '__main__':
    ck = environ["cookie"]
    SendKey = environ.get('SendKey')
    try:
        title, Text = CheckIn(ck)
    except Exception as e:
        title = '签到失败'
        Text = e
    finally:
        print(title)
        print(Text)
        send_msg(SendKey, title, Text)
