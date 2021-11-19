"""Запрос курса по коду валюты arg=String"""

from requests import get, utils
from datetime import datetime

response = get("http://www.cbr.ru/scripts/XML_daily.asp?VAL_NM_RQ=R01235")
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates(curr):

    index_rate = content.find('Value', content.find(curr.upper()))+6
    index_date = content.find('Date')+6
    date = datetime(year=int(content[index_date+6:index_date+10]),
                    month=int(content[index_date+3:index_date+5]),
                    day=int(content[index_date:index_date+2]))

    if index_rate != 5:
        rate = float(content[index_rate:index_rate+7].replace(',','.'))
    else:
        rate = None

    return rate, str(date)


if __name__ == '__main__':
    print(currency_rates('usd'))
