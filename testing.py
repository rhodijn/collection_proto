#!/usr/bin/env python3

#   ###################
#   ##                 ##
#   ##               ##
#     ######       ##
#       ##       ######
#     ##               ##
#   ##                 ##
#     ###################


import requests
from bs4 import BeautifulSoup

def suche_isbn(isbn):
    # construct the search url
    url = f"https://www.lehmanns.de/search?q={isbn}"

    # define the header
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/124.0 Safari/537.36'
        )
    }

    # send a request
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
        print("A request error occurred:", e)

    # parse html response
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract results
    treffer = soup.select('.product-item')
    if not treffer:
        print('Keine Treffer gefunden.')
        return

    for item in treffer[:5]:  # max. 5 Treffer ausgeben
        titel = item.select_one('.product-title').get_text(strip=True)
        preis = item.select_one('.price').get_text(strip=True)
        link  = item.select_one('a')['href']
        print(f"Titel: {titel}\nPreis: {preis}\nLink: https://www.lehmanns.de{link}\n")

# function call
suche_isbn('9783833898235')