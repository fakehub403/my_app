import requests

cookies = {
    'captcha_token': 'eyJleHAiOjE3Nzg3OTAwMDB9.7d707f5c633de699b3c5b43bb1f8d510a4f4e50353347a88e15ff119c1e939f8',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="148", "Brave";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    # 'cookie': 'captcha_token=eyJleHAiOjE3Nzg2NjAwMDB9.96a295b55f42027ff157535e40a04f115b4768cf86b25f1b8ebf59944b67afd9',
}


def send():
    files = {
        'q': f'site:{site} "@gmail.com"',
        'category_general': '1',
        'pageno': f'{num}',
        'language': 'auto',
        'time_range': '',
        'safesearch': '1',
        'theme': 'simple',
    }
    response = requests.post('https://priv.au/search', cookies=cookies,headers=headers, data=files)

send()


