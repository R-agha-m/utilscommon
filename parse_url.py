
class ParseUrl:
    def __init__(self, url):

        self.url_raw = url
        self.url_raw_lower = url.lower()

        self.protocols = ("http://", "https://", "ftp://", "ftps://", "socks4://", "socks5://")

        self.parsed_url = None
        self.url_without_protocol_with_www = None
        self.url_without_protocol_with_www_lower = None
        self.detected_protocol = None

    def perform(self):
        self._detect_protocol()
        self._detect_www()
        self._detect_domain()

        return {"scheme": self.protocol.replace("://", ""),
                "protocol": self.protocol,

                "url_without_protocol_without_www": self.url_without_protocol_without_www,
                "url_without_protocol_with_www": "www." + self.url_without_protocol_without_www,
                "url_with_protocol_without_www": self.protocol + self.url_without_protocol_without_www,
                "url_with_protocol_with_www": self.protocol + "www." + self.url_without_protocol_without_www,

                "domain_without_protocol_without_www": self.domain_without_protocol_without_www,
                "domain_without_protocol_with_www": "www." + self.domain_without_protocol_without_www,
                "domain_with_protocol_without_www": self.protocol + self.domain_without_protocol_without_www,
                "domain_with_protocol_with_www": self.protocol + "www." + self.domain_without_protocol_without_www}

    def _detect_protocol(self):
        for protocol in self.protocols:
            if self.url_raw_lower.startswith(protocol):
                self.url_without_protocol_with_www = self.url_raw[len(protocol):]
                self.url_without_protocol_with_www_lower = self.url_raw_lower[len(protocol):]
                self.protocol = protocol
                return
        else:
            self.url_without_protocol_with_www = self.url_raw
            self.url_without_protocol_with_www_lower = self.url_raw_lower
            self.protocol = 'http://'
            return

    def _detect_www(self):
        if self.url_without_protocol_with_www_lower.startswith("www."):
            self.url_without_protocol_without_www_lower = self.url_without_protocol_with_www_lower[4:]
            self.url_without_protocol_without_www = self.url_without_protocol_with_www[4:]
        else:
            self.url_without_protocol_without_www_lower = self.url_without_protocol_with_www_lower
            self.url_without_protocol_without_www = self.url_without_protocol_with_www

    def _detect_domain(self):
        self.domain_without_protocol_without_www = self.url_without_protocol_without_www.split("/")[0]


def parse_url(url):
    return ParseUrl(url).perform()
