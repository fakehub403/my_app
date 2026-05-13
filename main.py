import requests, time, random


headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://breach.vip',
    'priority': 'u=1, i',
    'referer': 'https://breach.vip/',
    'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Chromium";v="148.0.0.0", "Brave";v="148.0.0.0", "Not/A)Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'cookie': 'XhPbtNbRzEbIchorDHGu9Kz.d5smLkKzVgWbU9cbUmM-1778677046-1.2.1.1-gcPlXutc9FD9WfEcQGCdeeaboe0qBt_LcOX9xhYjpdYGcU64Jcivor3VnvQcjQD2WyXb.pd7.r9NjVb1_r6Btkr8Vz6I9uQaiUIfliVcFwaWTGAxYM.hHsxErLvxX9SHC9W8k2dAqP0OvvO28AdUbLIDtZIef0RajQA0nC4hoKUd1QxnSB5SlkgJEwnTcirIdeCF077q3zFXnJVDcZk8SJ78THuzjSHUeKZIB866JVo7_l5JkXwDW.V1CY_RfpRTtdnVkblpx7WTSoUNWTsmaBmSnWjLgY9TAGlUM9FbfpYg4E0Y7XCH15Ge0OIlexFPNNNGcFdKDcl.0miAKS3HZ8tMGWxFL0KT8TZAHd9NJlQGOVRTQGQe8Z7sIl3QOai48wJQjv7ySnqQ7bzBxRe4A8Zk7TQ0bSKiHy7uvrCaUKE',
}

json_data = {
    'term': 'vectra.ai',
    'fields': [
        'domain',
    ],
    'wildcard': False,
    'case_sensitive': False,
    'categories': [],
}

response = requests.post('https://breach.vip/api/search', headers=headers, json=json_data)
