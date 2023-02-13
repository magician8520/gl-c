from os import environ
from Check import CheckIn
from push import send_msg

if __name__ == '__main__':
    # 获取actions secrets配置的cookie SendKey
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
        # Text = Text.replace('\n', '%0D%0A%0D%0A')
        Text = Text.replace('\n', '%0A%0A')  # 替换\n，优化微信推送消息显示格式
        send_msg(SendKey, title, Text)  # 推送消息，无SendKey不推送
