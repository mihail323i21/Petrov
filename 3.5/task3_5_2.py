# import math
# from statistics import mean
# import pandas as pd
# import sqlite3
#
# s_cur_to_digits = {"BYR": 1, "USD": 2, "EUR": 3, "KZT": 4, "UAH": 5}
#
#
# def get_salary(s_from, s_to, s_cur, date):
#     year_month = date[1] + "/" + date[0]
#     s_cur_value = 0
#
#     if s_cur != "RUR" and (s_cur == s_cur) and s_cur in ["BYN", "BYR", "EUR", "KZT", "UAH", "USD"]:
#         s_cur.replace("BYN", "BYR")
#         cur.execute("SELECT * FROM CB_Currency WHERE date == :year_month", {"year_month": year_month})
#         s_cur_value = cur.fetchall()[0][s_cur_to_digits[s_cur]]
#     elif s_cur == "RUR":
#         s_cur_value = 1
#
#     if math.isnan(s_from) and not (math.isnan(s_to)):
#         return s_to * s_cur_value
#     elif not (math.isnan(s_from)) and math.isnan(s_to):
#         return s_from * s_cur_value
#     elif not (math.isnan(s_from)) and not (math.isnan(s_to)):
#         return mean([s_from, s_to]) * s_cur_value
#
#
# df = pd.read_csv("6.csv")
# con = sqlite3.connect("CB_Currency.db")
# cur = con.cursor()
#
# df["published_at"] = df["published_at"].apply(lambda date: date[:7])
# df["years"] = df["published_at"].apply(lambda date: date[:4])
# df.insert(1, "salary", df.apply(lambda row: get_salary(row["salary_from"], row["salary_to"], row["salary_currency"],
#                                                        row["published_at"].split("-")), axis=1))
# df.drop(["salary_from", "salary_to", "salary_currency"], axis=1, inplace=True)
# df = df[df["salary"].notnull()]
#
#
# connect = sqlite3.connect("new_vac_with_dif_currencies.db")
# cursor = con.cursor()
# df.to_sql(name="new_vac_with_dif_currencies", con=connect, if_exists='replace', index=False)
# connect.commit()
#
# print("Овинкин Кирилл Михайлович")