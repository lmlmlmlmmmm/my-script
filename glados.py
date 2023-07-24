import requests
import os

headers = {
    'cookie': ''
}

plans = {
    "0": "Free",
    "10": "Free",
    "11": "Education",
    "21": "Basic",
    "31": "Pro",
    "41": "Team",
    "51": "Enterprise"
}


def get_status():
    url = 'https://glados.rocks/api/user/status'
    res = requests.get(url=url, headers=headers)
    return res.json()


def checkin():
    url = 'https://glados.rocks/api/user/checkin'
    data = {
        'token': 'glados.network'
    }
    res = requests.post(url=url, headers=headers, data=data)
    return res.json()


def start():
    cookies = os.getenv("GLADOS_COOKIE")
    if not cookies:
        raise Exception("未设置 GLADOS_COOKIE 常量")

    cookie_list = cookies.split("@")

    for cookie in cookie_list:
        headers['cookie'] = cookie
        get_status_res = get_status()
        print(f'当前用户为：{get_status_res["data"]["email"]}, 会员PLAN为：{plans[str(get_status_res["data"]["vip"])]}, '
              f'剩余会员天数为：{int(float(get_status_res["data"]["leftDays"]))}')

        checkin_res = checkin()
        print(f'签到结果为：{checkin_res["message"]}')

        get_status_res = get_status()
        print(f'当前用户为：{get_status_res["data"]["email"]}, 会员PLAN为：{plans[str(get_status_res["data"]["vip"])]}, '
              f'剩余会员天数为：{int(float(get_status_res["data"]["leftDays"]))}')


start()
