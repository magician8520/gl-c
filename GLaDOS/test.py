# from os import environ
from push import send_msg
if __name__ == '__main__':
    # SendKey = environ.get('SendKey')
    SendKey = 'SCT193711TfIFJ6wSVn1WmDF0VUtaQaVPI'
    title = '这是一次测试'
    Text = '第一行 吧啦吧啦~\n第二行 吧啦吧啦~\n第三行 吧啦吧啦~'
    print(title)
    print(Text)
    # Text = Text.replace('\n', '%0D%0A%0D%0A')
    Text = Text.replace('\n', '%0A%0A')
    rsp = send_msg(SendKey, title, Text)

    print(rsp)
