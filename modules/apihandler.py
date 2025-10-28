#!/usr/bin/env python3

#   ###################
#   ##                 ##
#   ##               ##
#     ######       ##
#       ##       ######
#     ##               ##
#   ##                 ##
#     ###################


import json, requests


def api_request(api_url: str, api_key: str, method: str, value: str, frmt: str, par_1: str, par_2='') -> dict:
    """
    perform an api request and return the answer

    parameters:
    method: str = api request method (GET, PUT, POST, ...)
    value: str = item id
    frmt: str = format (json, xml)
    param_1: str = api parameter 1
    param_2: str = api parameter 2

    returns:
    data: dict = {}
    """
    req = False
    resp = False

    if method == 'get':
        try:
            req = f"{api_url}{par_1}{value}{par_2}&apikey={api_key}&format={frmt}"
            resp = requests.get(req)
            data = json.loads(resp.content.decode(encoding='utf-8'))
        except Exception as e:
            resp = e
    return data