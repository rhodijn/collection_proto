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


def api_request(api_url: str, api_key: str, method: str, value: str, frmt: str, par_1: str, par_2='', log=True) -> dict:
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

    if log:
        column_names = ['api_call', 'status_code']
        delim = ';'
        filepath = 'files/log'

        try:
            df_log = pd.DataFrame(pd.read_csv(f"{filepath}/log_apihandler.csv", dtype=str, sep=delim))
        except:
            df_log = pd.DataFrame(columns=column_names)

    if method == 'get':
        try:
            req = f"{api_url}{par_1}{value}{par_2}&apikey={api_key}&format={frmt}"
            resp = requests.get(req)
            data = resp.json()
        except Exception as e:
            resp = e

    if log:
        df_log.loc[len(df_log)] = {'api_call':req, 'status_code': resp.status_code}
        df_log.to_csv(f"{filepath}/log_apihandler.csv", sep=delim, index=False, header=True)

    return data