import requests
from datetime import date, timedelta

"""
"r030":36,
"txt":"Австралійський долар",
"rate":16.5223,
"cc":"AUD",
"exchangedate":"01.01.2020"
"""

class Rate:
    def __init__(self, currency, value, date):
        self.currency = currency
        self.value = value
        self.date = date

def rating(dictionary):
    instance = Rate(
        currency = dictionary["cc"],
        value = dictionary["rate"],
        date = dictionary["exchangedate"]
    )
    return instance

def period_load(start_date: date, end_date: date, currency_cc: str):
    mainList = []
    for index in range(0, (end_date - start_date).days + 1):
        request_date = ''.join(str(start_date + timedelta(days = index)).split('-'))
        request = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={request_date}&json')
        currency_listed = [rating(dictionary) for dictionary in request.json() if rating(dictionary).currency == currency_cc]
        mainList += currency_listed
    return [(index.currency, index.value, index.date) for index in mainList]

def average(result):
    average = 0
    for tupled_currency in result:
        average += tupled_currency[1]
    return average / len(result) 
