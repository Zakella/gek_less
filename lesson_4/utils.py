import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from decimal import Decimal


def currency_rates(code, return_date=False, dec=False):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    if response.status_code == 200:
        root = ET.fromstring(response.text)
        dict_currency = {}
        for val in root.findall('Valute'):
            dict_currency[val.find('CharCode').text.lower()] = {
                "Value": float(val.find('Value').text.replace(',', '.')),
                "NumCode": val.find('NumCode').text,
                "Nominal": val.find('Nominal').text,
                "Name": val.find('Name').text}
    if code.lower() in dict_currency:
        value = dict_currency[code.lower()]["Value"]
        if dec:
            value = Decimal.from_float(value)
        date_time_obj = ""
        if return_date:
            for date in root.attrib.values():
                break
            date_time_obj = datetime.strptime(date, "%m.%d.%Y").date().today()
    return f"{value},{date_time_obj}"
