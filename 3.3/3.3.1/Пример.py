import pandas as pd
import xml.etree.ElementTree as ET
from urllib.request import urlopen

pd.set_option("expand_frame_repr", False)
df = pd.read_csv("6.csv")

df_cur = df.groupby("salary_currency").size()
df_cur = df_cur.apply(lambda currency: currency if currency >= 5000 else False)

latest_earlier = [int(".".join(df["published_at"].min()[5:7].split("-"))),
                  int(".".join(df["published_at"].max()[5:7].split("-")))]

df_api_currency = pd.DataFrame(columns=["date", "BYR", "USD", "EUR", "KZT", "UAH"])

months = []

for year in range(2003, 2023):
    if year == 2022:
        for month in range(1, latest_earlier[1] + 1):
            if 1 <= month <= 9:
                months.append(f"0{month}/{year}")
            else:
                months.append(f"{month}/{year}")
    else:
        for month in range(latest_earlier[0], 13):
            if 1 <= month <= 9:
                months.append(f"0{month}/{year}")
            else:
                months.append(f"{month}/{year}")

for i in range(len(months)):
    tree = ET.parse(urlopen(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/{i}d=1"))
    root = tree.getroot()
    values = [i]
    for child in root.findall("Valute"):
        charcode = child.find("CharCode").text.replace("BYN", "BYR")
        if charcode in df_cur:
            value = float(child.find("Value").text.replace(",", "."))
            nominal = float(child.find("Nominal").text.replace(",", "."))
            values.append(value / nominal)
        print(child.find("CharCode").text)
    print(values)


    # df_api_currency.loc[i] = values

