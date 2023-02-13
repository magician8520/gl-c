from requests import post


def send_msg(SendKey, title, Text):

    if not SendKey:
        # 无SendKey则拦截推送
        return False
    url = f'https://sctapi.ftqq.com/{SendKey}.send?title={title}&desp={Text}'
    post(url=url)
