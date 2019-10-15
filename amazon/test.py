import requests
import json
from fake_useragent import UserAgent
headers = {
    'user-agent': UserAgent(verify_ssl=False).chrome
}
cookies = {'Cookie:session-id': '458-8053283-5409134', 'i18n-prefs': 'CNY', 'ubid-acbcn': '461-1200220-8056953', 'x-wl-uid': '1PWall/n62pMnBZ2JVc4ucbIUtk2qJuVXih3Dau9EUoC/9q9Nc7UiRDZJZXn/7Ft7Y6QnifC4mVY', 'lc-acbcn': 'zh_CN', 'cnm_gw_cnffpe_c1': '1568087006000', 'floatingBannerOnGateway': 'floatingBannerOnGateway', 'session-token': 'O0d1l7CSmveWAWqaFJYlrpjp9G9wog8mQ4YLmVpp5gCJgfM78LVi+OjcufSLOR9BZlIlZhXqYab7yn3YR1ehjM1Two7a9WBDWZkRxYVF3hvw/vi9iwHenAlUdlCIOTaqS1LZ47ThFVteJQWuspbxrjBZIggU3proI9mnyLhpQgq1bmedCzoq66ocDFSUwxdw', 'session-id-time': '2082729601l', 'csm-hit': 'tb:DPJ75RVJ8QS66TVRY22G+s-WFXS4WET1T6E698WVG6Y|1571040967770&t:1571040967770&adb:adblk_no'}
url = 'https://www.amazon.cn/s?k=女装'

html = requests.get(url,headers=headers, cookies=cookies).text

print(html)
