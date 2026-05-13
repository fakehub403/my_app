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
    'cookie': 'cf_clearance=BvVoCgkBKVxmn.MFl_q.yMlCY.o8XGmZYY66iv0Lrek-1778675187-1.2.1.1-J3vR6eeP5Rph_.jZ_5ybQpYF5ICxzfVbmm4eRmL9i1qZJFgqGnAoc_i3qZYqoWJcmVf0B3u87xZMojEqbuoRNGzMp3OwsI2Y3NB7hxeJQ8d4.OuBcQ5iJWka_fj3gr2bjohpb4ywTuSSsZgfTwo16t6M7rNpPjkCApurD_Hc2vPBNQkpPSOGwnXY6WZHphrSdsnfpikZVLhN7cDWx.Wv0Mv_G3vE7_QnMSQvDd8RGgJ_Nc3RpmvhtId.Pxj50NYgEK3324hZ.QsLTDLxaGlkxUYPY2NjN7GVvtj2uS1qEBHEdS0PueIZE81Od_leAbki6YhtGAVeZfEFSV2UftRMOniG9C3QUw2kO3xwZPBLi4ugimhLA_WbSMXjmkERtO5S5hnAcGxVZKIMUxgfIgrfqFcVke1qbMTiOq6UQbE4RLM',
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

while True:
    time.sleep(random.randint(4, 10))
    if response.status_code != 200:
        break
    else:
        print(response.status_code)
        continue
