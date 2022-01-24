import requests
import random
from random import shuffle

try:
    from .get_public_ip import get_public_ip
    from .exception import CannotCheckProxy
    from .stg import STG
except ImportError:
    from get_public_ip import get_public_ip
    from exception import CannotCheckProxy
    from stg import STG

user_agent = [
    'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20060814 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43',
]
headers = {'User-Agent': random.choice(user_agent), }

sites_2_judges_proxy = ['http://proxyjudge.us',
                        'http://azenv.net/',
                        'http://httpheader.net/azenv.php',
                        'http://mojeip.net.pl/asdfa/azenv.php']

shuffle(sites_2_judges_proxy)

sites_2_get_my_geo = ['http://ipwhois.app/json/{0}',
                      'http://ip-api.com/json/{0}',
                      'https://api.techniknews.net/ipgeo/{0}']

shuffle(sites_2_get_my_geo)


class ProxyChecker:
    def __init__(self,
                 proxy,
                 time_out=STG.TIME_OUT,
                 get_geo=True):

        self.proxy = proxy
        self.time_out = time_out
        self.get_geo = get_geo

        # 'https://user:password@proxyip:port'
        self.proxy_dict = {
            f'{self.proxy["protocol"]}':
                f'{self.proxy["protocol"]}://'
                f'{self.proxy["username"]}:{self.proxy["password"]}@'
                f'{self.proxy["host"]}:{self.proxy["port"]}',
        }

        self.results = dict()
        self.ip = None

    def perform(self):
        self._get_my_ip()
        self._judge_proxy()
        if self.get_geo:
            self._get_geo()
        return self.results

    def _get_my_ip(self):
        self.ip = get_public_ip()

    def _judge_proxy(self):
        for site in sites_2_judges_proxy:
            response = requests.get(url=site,
                                    proxies=self.proxy_dict,
                                    headers=headers,
                                    timeout=self.time_out)

            if response.status_code == 200:
                self.results['status'] = 'successful'
                self.results['status_code'] = response.status_code
                self.results['response'] = response.text
                self.results['anonymity'] = 'Transparent' if self.ip in response.text else 'Anonymous'
                return
        raise CannotCheckProxy

    def _get_geo(self):
        for site in sites_2_get_my_geo:
            response = requests.get(url=site.format(self.proxy["host"]),
                                    headers=headers,
                                    timeout=self.time_out)
            if response.status_code == 200:
                self.results.update(response.json())
                return
        raise CannotCheckProxy


if __name__ == "__main__":
    obj = ProxyChecker({"protocol": "http",  # http, https, socks4, socks5
                        "host": "192.142.225.78",
                        "port": "45785",
                        "username": "Selyelenasoft",
                        "password": "Q1q7PeI"})
    results = obj.perform()
    print(results)
