#-*- coding: utf-8 -*-
import requests
import xmltodict


currency_table_xml = requests.get("https://www.nbp.pl/kursy/xml/a014z230120.xml")
currency_table_xml.encoding = 'ISO-8859-2'
currency_dic = xmltodict.parse(currency_table_xml.text)['tabela_kursow']['pozycja']
currency_table_xml.close()

gold_price_xml = requests.get("https://www.nbp.pl/aspx/Cena_zlota.aspx" )
gold_price_dic = xmltodict.parse(gold_price_xml.text)['cena']
gold_price_xml.close()
