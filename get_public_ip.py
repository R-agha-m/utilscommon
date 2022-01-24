from re import compile
from os import environ
from socket import gethostbyname, gethostname
from requests import request
from traceback import print_exc

try:
    from .run_command import run_command
    from .exception import CannotGetIPAddress, IPFound
    from .parse_url import parse_url
except ImportError:
    from run_command import run_command
    from exception import CannotGetIPAddress, IPFound
    from parse_url import parse_url

__all__ = ("get_public_ip", "GetPublicIp",)

default_commands = (["dig", "+short", "myip.opendns.com", "@resolver1.opendns.com"],)

default_sites = ("http://httpbin.org/ip",
                 "http://icanhazip.com",
                 "http://ident.me",
                 "http://ifconfig.me/ip",
                 "http://ifconfig.io/ip",
                 "http://ipinfo.io/ip",
                 "http://ipecho.net/plain",
                 'http://ipwhois.app/json/',
                 'http://ip-api.com/json/')

default_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Host": "<should be written before request>",
    "Referer":	"https://www.google.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


class GetPublicIp:
    def __init__(self,
                 commands=default_commands,
                 sites=default_sites,
                 headers=default_headers):

        self.commands = commands
        self.sites = sites
        self.headers = headers

        self.ip = None

    def perform(self):
        try:
            self._get_from_env_var()
            self._get_from_socket()
            self._get_ip_by_request()
            self._get_ip_by_commands()
            raise CannotGetIPAddress
        except IPFound:
            return self.ip

    def _get_from_env_var(self):
        ip = environ.get("IP", None)
        self._is_public_ip(ip=ip)

    def _get_from_socket(self):
        ip = gethostbyname(gethostname())
        self._is_public_ip(ip=ip)

    def _get_ip_by_request(self):
        for site in self.sites:
            try:
                headers = self.headers.copy()
                headers["Host"] = parse_url(site)["url_without_protocol_without_www"]
                data = request(method="get",
                               url=site,
                               headers=headers)

                self._extract_ip(data=data.text)
            except IPFound:
                raise
            except Exception:
                print_exc()

    def _get_ip_by_commands(self):
        for command in self.commands:
            try:
                data = run_command(command=command,
                                   raise_error=True)

                self._extract_ip(data=data)
            except IPFound:
                raise
            except Exception:
                print_exc()

    def _extract_ip(self, data):
        data = data.replace("\n", "")

        # extract ip format strings
        re_compile = compile(r"[0-9.]+")
        ip_list = set(re_compile.findall(data))

        # check ip validity
        for raw_ip in ip_list:
            re_compile = compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)"
                                 r"{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
            detected_ip = re_compile.match(raw_ip)
            if detected_ip:
                self._is_public_ip(ip=detected_ip[0])
        return

    def _is_public_ip(self, ip):
        if not ip:
            return False

        ip = str(ip)

        if ip.startswith(("127.", "10.", "192.168.")):
            return False

        self.ip = ip
        raise IPFound


def get_public_ip():
    return GetPublicIp().perform()


