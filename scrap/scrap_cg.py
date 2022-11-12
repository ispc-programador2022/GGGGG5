
import json
import requests
import pandas as pd
import csv
from pprint import pprint

from bs4 import BeautifulSoup




def get_heading(table):
    '''Obtenemos los encabezados de la tabla desde la web'''
    heading = list()
    thead = table.find('thead').find('tr').find_all('th')[0:5]

    for th in thead:
        heading.append(th.text)

    return heading



def extract_data(table):
    '''Obtenemos los datos de la tabla'''
    crypto_list = list()
    tbody = table.find('tbody').find_all('tr')
    tbodyth = table.find('tbody').find_all('th')
    for i, tr in enumerate(tbody):
        tds = tr.find_all('td')[0:5]
        crypto_list.append((
            tbodyth[i].text,
            tds[0].text,
            tds[1].text,
            tds[2].text,
            tds[3].text,
            ))

    return crypto_list

def main_scrap():
    crypto_data = []
    #url = f'https://www.coingecko.com/es/monedas/bitcoin/historical_data?page={pagina}&end_date=2022-11-11&start_date=2021-01-01'
    
    for i in range(10):
        pagina = 1 + i
        url = f'https://www.coingecko.com/en/coins/bitcoin/historical_data?page={pagina}&start_date=2021-01-01&end_date=2022-11-11'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        crypto_data.append(extract_data(table))
    crypto_data_flat = []
    for i in crypto_data:
        for l in i:
            crypto_data_flat.append(l)

    heading = get_heading(table)

    return heading, crypto_data_flat

    # with open('cryptos_price.csv', 'w') as f:
    #     write = csv.writer(f)
    #     write.writerow(heading)
    #     write.writerows(crypto_data_flat)


if __name__ == '__main__':
    main_scrap()