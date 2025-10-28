#!/usr/bin/env python3


#   ###################
#   ##                 ##
#   ##               ##
#     ######       ##
#       ##       ######
#     ##               ##
#   ##                 ##
#     ###################


# this script generates a friendly list of titles, authors (including editions) from a list of barcodes


import os
import pandas as pd

from dotenv import dotenv_values
from modules.apihandler import *


SECRETS = dotenv_values('.env')

barcodes : list = []
delim = ';'
files = []
filepath = 'files'


# scan folder and exclude subfolders
files = os.listdir(f"{filepath}/input")
files = [f for f in files if os.path.isfile(f"{filepath}/input/{f}")]


# find the first csv-file in the folder
for k, v in enumerate(files):
    parts = v.split('.')
    if parts[-1] == 'csv':
        ind = k

print(f"File: {files[ind]}")


# generate datafrome from csv-file, capitalize the barccode column
df_rp_loeschen = pd.DataFrame(pd.read_csv(f"{filepath}/input/{files[ind]}", dtype=str, sep=delim))
df_rp_loeschen['barcode'] = df_rp_loeschen['barcode'].str.upper()


for i, el in enumerate(df_rp_loeschen['barcode']):
    item_info = api_request(SECRETS['API_URL'], SECRETS['API_KEY'], 'get', el, 'json', 'items?item_barcode=')
    try:
        df_rp_loeschen.loc[i, 'call_number'] = item_info['holding_data']['call_number']
    except Exception as e:
        df_rp_loeschen.loc[i, 'call_number'] = e
    try:
        df_rp_loeschen.loc[i, 'title'] = item_info['bib_data']['title']
    except Exception as e:
        df_rp_loeschen.loc[i, 'title'] = e
    try:
        df_rp_loeschen.loc[i, 'author'] = item_info['bib_data']['author']
    except Exception as e:
        df_rp_loeschen.loc[i, 'author'] = e
    try:
        df_rp_loeschen.loc[i, 'isbn'] = item_info['bib_data']['isbn']
    except Exception as e:
        df_rp_loeschen.loc[i, 'isbn'] = e
    try:
        df_rp_loeschen.loc[i, 'complete_edition'] = item_info['bib_data']['complete_edition']
    except Exception as e:
        df_rp_loeschen.loc[i, 'complete_edition'] = e
    try:
        df_rp_loeschen.loc[i, 'date_of_publication'] = item_info['bib_data']['date_of_publication']
    except Exception as e:
        df_rp_loeschen.loc[i, 'date_of_publication'] = e

try:
    df_rp_loeschen.to_csv(f"{filepath}/output/output.csv", sep=delim)
except Exception as e:
    print(f"an error occurred: {e}")