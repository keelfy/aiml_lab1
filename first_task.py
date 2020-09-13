# basic stuff
import random
import json
import datetime
import string
import time
import os
# structural
import xml.etree.ElementTree as XmlElementTree
from pprint import pprint
from typing import Set, List, Dict, Callable, Iterator
import requests
import numpy as np
import scipy.sparse as sparse
# plotter
import matplotlib.pyplot as plt
import matplotlib

# Subtask 1
array = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']
result = {value: [idx for idx, x in enumerate(array) if x == value] for value in array}
print(f'Subtask #1 (a/b) = {result}')


# Subtask 2
def similarity_calculator(lhs: Set, rhs: Set) -> float:
    intersection_counter = 0
    for lhv in lhs:
        for rhv in rhs:
            if lhv == rhv:
                intersection_counter += 1

    union = len(lhs) + len(rhs) - intersection_counter
    return intersection_counter / union


def create_set(length: int, generator: callable, generator_args: tuple = None) -> set:
    res = set()     # Resulting set
    while len(res) != length:
        element = generator(*generator_args) if generator_args is not None else generator()
        res.add(element)
    return res


set1 = create_set(50, random.randint, (-100, 100))
set2 = create_set(50, random.randint, (-100, 100))
print(f'Subtask #2 = {similarity_calculator(set1, set2)}')


# Subtask 4
url = r'https://raw.githack.com/keelfy/aiml_lab1/master/resources/sales.json'
data = json.loads(requests.get(url).text)
csv_data = list()
csv_data.append(["item", "country", "year", "sales"])

for json_item in data:
    item_name = json_item['item']
    for country in json_item['sales_by_country']:
        for year in json_item['sales_by_country'][country]:
            sales = json_item['sales_by_country'][country][year]
            csv_data.append([item_name, country, year, sales])
pprint(csv_data)


# Subtask 5
def get_day_formatted(date: datetime.date) -> str:
    day = str(date.day)
    return day if len(day) == 2 else '0' + day


def get_month_formatted(date: datetime.date) -> str:
    month = str(date.month)
    return month if len(month) == 2 else '0' + month


begin_date = datetime.date.fromisoformat('2020-03-01')
end_date = datetime.date.fromisoformat('2020-07-01')
total_days = (end_date - begin_date).days
delta = datetime.timedelta(days=1)

request_url = r'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
required_valuetes = ['USD', 'EUR', 'INR', 'UAH']
required_valuetes_data = {valuete: list() for valuete in required_valuetes}
session = requests.session()

current_date = begin_date
while current_date != end_date:
    day = get_day_formatted(current_date)
    month = get_month_formatted(current_date)
    year = str(current_date.year)

    web_request = request_url + f'{day}/{month}/{year}'
    data = session.get(web_request)
    xml = XmlElementTree.fromstring(data.text)

    for valuete in xml:
        valuete_name = valuete[1].text
        valuete_cost = float(valuete[4].text.replace(',', '.')) / float(
            valuete[2].text.replace(',', '.'))

        if valuete_name in required_valuetes:
            required_valuetes_data[valuete_name].append(valuete_cost)

    # going to the next day...
    current_date += delta

print('Subtask #5 = {')
for valuete in required_valuetes:
    print(f'{valuete} = {required_valuetes_data[valuete]}')
print('}')
