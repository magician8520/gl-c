from requests import post, get
from datetime import datetime, timedelta


def send_msg(SendKey, title, Text):

    if not SendKey:
        # 无SendKey则拦截推送
        return False
    url = f'https://sctapi.ftqq.com/{SendKey}.send?title={title}&desp={Text}'
    rsp = post(url=url)
    pushid = rsp.json()['data']['pushid']
    readkey = rsp.json()['data']['readkey']
    status_url = f'https://sctapi.ftqq.com/push?id={pushid}&readkey={readkey}'
    stop_time = datetime.now() + timedelta(minutes=1, seconds=0)
    while True:
        status_rsp = get(url=status_url)
        result = status_rsp.json()['data']['wxstatus']
        if result:
            return '消息推送成功！'
        elif datetime.now() >= stop_time:
            return '程序运行结束！推送未成功！'
