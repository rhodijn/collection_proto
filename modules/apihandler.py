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
from dotenv import dotenv_values

SECRETS = dotenv_values('.env')


def api_request(method: str, value: str, frmt: str, par_1: str, par_2='') -> tuple:
    """
    perform an api request and return the answer

    parameters:
    method: str = api request method (GET, PUT, POST, ...)
    value: str = item id
    frmt: str = format (json, xml)
    param_1: str = api parameter 1
    param_2: str = api parameter 2

    returns:
    tuple = (req: str, response: requests.models.Response)
    """
    resp = False

    if method == 'get':
        req = f"{SECRETS['API_URL']}{par_1}{value}{par_2}&apikey={SECRETS['API_KEY']}&format={frmt}"
        resp = requests.get(req)
    return req, resp