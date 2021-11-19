# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату
# из ответа, какой тип данных лучше использовать в ответе функции?

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


print(currency_rates('usd'))





