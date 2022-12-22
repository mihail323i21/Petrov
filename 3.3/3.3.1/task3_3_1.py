import pandas as pd
import requests

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
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=15/{months[i]}d=1"
    response = requests.get(url)
    cur_df = pd.read_xml(response.text)
    cur_filtered_df = cur_df.loc[cur_df['CharCode'].isin(["BYN", "BYR", "EUR", "KZT", "UAH", "USD"])]

    BYR_v = float(
        cur_filtered_df.loc[cur_filtered_df["CharCode"].isin(["BYR", "BYN"])]["Value"].values[0].replace(',', "."))
    EUR_v = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "EUR"]["Value"].values[0].replace(',', "."))
    KZT_v = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "KZT"]["Value"].values[0].replace(',', "."))
    UAH_v = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "UAH"]["Value"].values[0].replace(',', "."))
    USD_v = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "USD"]["Value"].values[0].replace(',', "."))

    BYR_n = float(cur_filtered_df.loc[cur_filtered_df["CharCode"].isin(["BYR", "BYN"])]["Nominal"].values[0])
    EUR_n = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "EUR"]["Nominal"].values[0])
    KZT_n = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "KZT"]["Nominal"].values[0])
    UAH_n = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "UAH"]["Nominal"].values[0])
    USD_n = float(cur_filtered_df.loc[cur_filtered_df["CharCode"] == "USD"]["Nominal"].values[0])

    BYR = BYR_v / BYR_n
    EUR = EUR_v / EUR_n
    KZT = KZT_v / KZT_n
    UAH = UAH_v / UAH_n
    USD = USD_v / USD_n

    df_api_currency.loc[i] = [months[i], BYR, EUR, KZT, UAH, USD]

df_api_currency.to_csv("CB_Currency.csv", index=False)