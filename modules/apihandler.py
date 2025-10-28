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
import pandas as pd


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
    column_names = ['api_call', 'response']
    delim = ';'
    filepath = 'files/log'
    req = False
    resp = False

    
    try:
        df_log = pd.read_csv(f"{filepath}/logfile.csv", names=column_names)
    except:
        df_log = pd.DataFrame(columns=column_names)

    if method == 'get':
        try:
            req = f"{api_url}{par_1}{value}{par_2}&apikey={api_key}&format={frmt}"
            resp = requests.get(req)
            data = resp.json()
        except Exception as e:
            resp = e

    df_log.loc[len(df_log)] = {'api_call': req, 'response': resp}
    df_log.to_csv(f"{filepath}/logfile.csv", sep=delim)

    return data