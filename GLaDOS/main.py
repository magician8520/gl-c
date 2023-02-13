from os import environ
from Check import CheckIn
from push import send_msg

if __name__ == '__main__':
    ck = environ["cookie"]
    SendKey = environ.get('SendKey')
    try:
        title, Text = CheckIn(ck)
        print('签到成功！')
    except Exception as e:
        print('签到失败！')
        title = '签到失败！'
        Text = e
    finally:
        # print(title)
        print(Text)
        Text = Text.replace('\n', '%0D%0A%0D%0A')
        send_msg(SendKey, title, Text)
