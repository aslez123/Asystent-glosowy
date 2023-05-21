from datetime import datetime

import requests
import xmltodict

from convert_date import convert_date
from xml_files import currency_dic


def assistant_convert_currency(currency_1, quantity):
    for k in currency_dic:
        if currency_1 == k['nazwa_waluty']:
            course = k['kurs_sredni'].replace(",", ".")
            try:
                return "Po zamianie {q} {c} na złotówki otrzymasz: {s} złotych".format(q=quantity, c=currency_1,
                                                                                       s=(float(quantity) * float(
                                                                                           course)))
            except ValueError:
                return "Podana ilość musi być liczbą"
    return 'Nie posiadam danej waluty w bazie'


def assistant_value(currency):
    for k in currency_dic:
        if currency == k['nazwa_waluty']:
            return "Kurs {currency} w dniu dzisiejszym wynosi {course}".format(currency=k['nazwa_waluty'], course=k['kurs_sredni'])
    return 'Nie znam odpowiedzi'


def assistant_archive_currency(currency, date):
    for i in date.split(' '):
        if i == 'roku':
            date = date.replace(' roku', '')
    try:
        new_date = datetime.strptime(convert_date(date), "%d %m %Y")
        new_date = new_date.strftime("%Y-%m-%d")
        currency_archives_table_xml = requests.get(
            "https://api.nbp.pl/api/exchangerates/tables/A/{}/?format=xml".format(new_date))
        currency_archives_dic = \
        xmltodict.parse(currency_archives_table_xml.text)['ArrayOfExchangeRatesTable']['ExchangeRatesTable']['Rates'][
            'Rate']
        for k in currency_archives_dic:
            if currency == k['Currency']:
                return "Kurs {currency} {date} roku wynosił {course}".format(currency=k['Currency'], date=date,
                                                                          course=k['Mid'])
    except:
        return "Błąd daty"
    return 'Nie znam odpowiedzi'


def assistant_archive_gold(date):
    for i in date.split(' '):
        if i == 'roku':
            date = date.replace(' roku', '')
    try:
        new_date = datetime.strptime(convert_date(date), "%d %m %Y")
        new_date = new_date.strftime("%Y-%m-%d")
        gold_archives_table_xml = requests.get("http://api.nbp.pl/api/cenyzlota/{}/?format=xml".format(new_date))
        gold_archives_dic = xmltodict.parse(gold_archives_table_xml.text)["ArrayOfCenaZlota"]["CenaZlota"]
    except:
        return 'Błąd daty"'
    return "Cena złota {date} roku wynosiła {p}".format(date=date, p=gold_archives_dic['Cena'])



