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

# Subtask #1
array = ['a', 'b', 'c', 'd', 'e', 'a', 'a', 'b', 'c']
result = {value: [idx for idx, x in enumerate(array) if x == value] for value in array}
print(f'Subtask #1 (a/b) = {result}')


# Subtask #2
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


# Subtask #4
url = r'https://jsonplaceholder.typicode.com/todos'
data = json.loads(requests.get(url).text)
csv_data = list()
csv_data.append(["userId", "id", "title", "completed"])

for json_item in data:
    item_name = json_item['item']
    for country in json_item['sales_by_country']:
        for year in json_item['sales_by_country'][country]:
            sales = json_item['sales_by_country'][country][year]
            csv_data.append([item_name, country, year, sales])

pprint(csv_data)

# saving solution file
with open('output.csv', 'w') as file:
    # MS Excel uses ';' to separate csv files
    # replace with ',' to use traditional CSV-file approach
    delimiter = ';'

    for row in csv_data:
        for column_index in range(len(row) - 1):
            file.write(row[column_index] + delimiter)
        file.write(str(row[len(row) - 1]) + '\n')