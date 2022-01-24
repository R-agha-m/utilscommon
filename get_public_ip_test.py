from requests import request
from re import compile
from os import environ
from socket import gethostbyname, gethostname
from requests import request
from traceback import print_exc

try:
    from .parse_url import parse_url
    from .exception import CannotGetIPAddress, IPFound
    from .valid_http_headers import headers
except ImportError:
    from parse_url import parse_url
    from exception import CannotGetIPAddress, IPFound
    from valid_http_headers import headers


default_sites = ("http://httpbin.org/ip",
                 "http://icanhazip.com",
                 "http://ident.me",
                 "http://ifconfig.me/ip",
                 "http://ifconfig.io/ip",
                 "http://ipinfo.io/ip",
                 "http://ipecho.net/plain",
                 'http://ipwhois.app/json/',
                      'http://ip-api.com/json/',)


default_headers = headers


def _extract_ip(data):
    data = data.replace("\n", "")

    # extract ip format strings
    re_compile = compile(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
    ip_list = set(re_compile.findall(data))

    # check ip validity
    for raw_ip in ip_list:
        re_compile = compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)"
                             r"{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        detected_ip = re_compile.match(raw_ip)
        if detected_ip:
            _is_public_ip(ip=detected_ip[0])
    return

def _is_public_ip(ip):
    if not ip:
        return False

    ip = str(ip)

    if ip.startswith(("127.", "10.", "192.168.")):
        return False

    print(ip)


for site in default_sites:
    headers = default_headers.copy()
    headers["Host"] = parse_url(site)["domain_without_protocol"]
    a = 1
    data = request(method="get",
                   url=site,
                   headers=headers,
                   timeout=10)

    if data.status_code != 200:
        a = 1

    print(f"---------------------{site}")
    print(data.text)

    _extract_ip(data.text)