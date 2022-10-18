import csv
import os
import requests
import json
import sys


def lookup(symbol: str, time_period="1m") -> tuple:
    symbol = symbol.upper()
    time_period = time_period.lower()
    response = requests.get(
        f"https://cloud.iexapis.com/stable/stock/{symbol}/chart/{time_period}/?token=pk_367412694e184c709f74251292922cdd"
    )

    try:
        response = response.json()
    except:
        sys.exit("API not working!")

    details = []
    for data in response:
        details.append({
            "high": data["high"],
            "low": data["low"],
            "close": data["close"],
            "symbol": data["symbol"],
            "date": data["date"],
            "timePeriod": time_period,
        })

    return details



def look_and_save(details: list, filename="details.csv"):
    with open(filename, 'r+', newline='') as file:
        reader = csv.DictReader(file)
        fieldnames = ['symbol', 'date', 'high', 'low', 'close', 'timePeriod',]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if os.stat(filename).st_size == 0:
            writer.writeheader()

        flag = False
        for i in details:
            for j in reader:
                if i["symbol"] == j["symbol"] and i["date"] == j["date"]:
                    flag = True
                    break
            if not flag:
                writer.writerow(i)

        
def write_details(details: list, filename="details.csv"):
    old_details = read_csv
    with open(filename, 'w', newline='') as file:
        fieldnames = ['symbol', 'date', 'high', 'low', 'close', 'timePeriod',]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if os.stat(filename).st_size == 0:
            writer.writeheader()

        flag = False
        for i in details:
            for j in old_details:
                if i["symbol"] == j["symbol"] and i["date"] == j["date"]:
                    flag = True
                    break
            if not flag:
                writer.writerow(i)


def update_csv(symbol):
    time = "1m"
    filename = "details.csv"
    if os.stat(filename).st_size != 0:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for i in reader:
                time = i["timePeriod"]

    details = lookup(symbol, time)
    look_and_save(details)


def read_csv(filename="details.csv"):
    file_exist = os.path.isfile(filename)
    if not file_exist:
        with open(filename, 'w'):
            pass

    with open(filename, 'r+') as file:
        details = csv.DictReader(file)
        details = list(details)

    return details


def get_csv():
    tmp = read_csv()

    dates = []
    namePrice = {}
    for i in tmp:
        if i["date"] not in dates:
            dates.append(i["date"])

        if i["symbol"] not in namePrice:
            namePrice[i["symbol"]] = {}
        
        if "close" not in namePrice[i["symbol"]]:
            namePrice[i["symbol"]]["close"] = []
        
        namePrice[i["symbol"]]["close"].append(i["close"])
    

    rgbs = [
        "#FF5555", "#55FF55", "#5555FF", "#FF00CC",
        "#0000FF", "#000000", "#FF0000", "#00FF00",
        "#6600CC", "#CC0066", "#009900", "#FF0066"
    ]
    j = 0
    for i in namePrice:
        namePrice[i]["rgb"] = rgbs[j]
        j += 1


    return (dates, namePrice)

def write_to_csv(details, filename="details.csv"):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['symbol', 'date', 'high', 'low', 'close',]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in details:
            if row["symbol"] != symbol:
                writer.writerow(row)


def remove_stock(symbol: str, filename="details.csv"):
    symbol = symbol.upper()
    details = read_csv()
    with open(filename, 'w', newline='') as file:
        fieldnames = ['symbol', 'date', 'high', 'low', 'close', 'timePeriod',]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in details:
            if row["symbol"] != symbol:
                writer.writerow(row)


def change_time(time):
    details = read_csv()
    symbols = []
    for i in details:
        if i["symbol"] not in symbols:
            symbols.append(i["symbol"])

    all_details = []
    for i in range(len(symbols)):
        for j in lookup(symbols[i], time):
            all_details.append(j)
    
    with open("details.csv", 'w', newline='') as file:
        fieldnames = ['symbol', 'date', 'high', 'low', 'close', 'timePeriod',]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_details:
            writer.writerow(row)
