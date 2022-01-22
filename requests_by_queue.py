from requests import request
from queue import Queue
from traceback import format_exc


def request_by_queue(input_queue, output_queue):
    while input_queue.qsize():
        try:
            item = input_queue.get()
            results = request(
                method=item.get("method", "get").upper(),
                # method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
                url=item["url"],  # url: URL for the new :class:`Request` object.
                params=item.get("params", None),
                # params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
                data=item.get("data", None),
                # data: (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`.
                headers=item.get("headers", None),
                # headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
                cookies=item.get("cookies", None),
                # cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
                files=item.get("files", None),
                # files: (optional) Dictionary of ``'filename': file-like-objects``for multipart encoding upload.
                auth=item.get("auth", None),
                # auth: (optional) Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth.
                timeout=item.get("timeout", None),
                # timeout: (optional) How long to wait for the server to send data before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
                allow_redirects=item.get("allow_redirects", True),
                # allow_redirects: (optional) Set to True by default.
                proxies=item.get("proxies", None),
                # proxies:(optional) Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
                hooks=item.get("hooks", None),
                stream=item.get("stream", None),
                # stream: (optional) whether to immediately download the response content. Defaults to ``False``.
                verify=item.get("verify", None),
                # verify:(optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string,
                cert=item.get("cert", None),
                # cert:(optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
                json=item.get("json", None),  # json: (optional) json to send in the body of the :class:`Request`.
            )

            output_queue.put({"item": item, "results": results})
            input_queue.task_done()

        except Exception:
            print(format_exc())


if __name__ == "__main__":
    input_queue = Queue()
    output_queue = Queue()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        # "Dnt": "1",
        # Do Not Track is a no longer official HTTP header field, designed to allow internet users to opt-out of tracking by websites—which includes the collection of data regarding a user's activity
        "Host": "httpbin.org",
        "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-61daa164-59aacf942814c3786286de4f"
    }
# ------------------------------------------------
    # Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # Accept-Encoding: "gzip, deflate, br",
    # Accept-Language: "en-US,en;q=0.9,fa;q=0.8",
    #
    # Host: "httpbin.org",
    # Sec-Ch-Ua: ""Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"",
    # Sec-Ch-Ua-Mobile: "?0",
    # Sec-Ch-Ua-Platform: ""Linux"",
    # Sec-Fetch-Dest: "document",
    # Sec-Fetch-Mode: "navigate",
    # Sec-Fetch-Site: "none",
    # Sec-Fetch-User: "?1",
    # Upgrade-Insecure-Requests: "1",
    # User-Agent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    # X-Amzn-Trace-Id: "Root=1-61daa2a0-4ce42a92317863ae589bd237"
# --------------------------------------
#     Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # Accept-Encoding: "gzip, deflate, br",
    # Accept-Language: "en-GB,en-US;q=0.9,en;q=0.8,fa;q=0.7",
    # Host: "httpbin.org",
    # Sec-Ch-Ua: "" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"",
    # Sec-Ch-Ua-Mobile: "?0",
    # Sec-Ch-Ua-Platform: ""Windows"",
    # Sec-Fetch-Dest: "document",
    # Sec-Fetch-Mode: "navigate",
    # Sec-Fetch-Site: "cross-site",
    # Sec-Fetch-User: "?1",
    # Upgrade-Insecure-Requests: "1",
    # User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    # X-Amzn-Trace-Id: "Root=1-61daa2d8-040d9a7f1ba962ed21e12643"
    # }


    proxies = {
        "http": "http://Selyelenasoft:Q1q7PeI@181.215.217.213:45785",
        "https": "http://Selyelenasoft:Q1q7PeI@181.215.217.213:45785",  # https should use http instead of https
    }

    # proxies = None

    for index in range(10):
        input_queue.put({"method": "get",
                         "url": "https://httpbingo.org/ip",
                         "params": None,
                         "data": None,
                         "headers": headers,
                         "cookies": None,
                         "files": None,
                         "auth": None,
                         'timeout': 10,
                         'allow_redirects': True,
                         'proxies': proxies,
                         'hooks': None,
                         'stream': None,
                         'verify': None,
                         'cert': None,
                         'json': None,
                         })

    request_by_queue(input_queue=input_queue,
                     output_queue=output_queue)

    a = 1
