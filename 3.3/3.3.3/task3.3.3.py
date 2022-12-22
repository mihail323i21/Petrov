import pandas as pd
import requests

pd.set_option("expand_frame_repr", False)

# Меняем интервалы времени публикации вакансии, чтобы выгрузить больше 2000 вакансий
all_urls = []
for i in range(1, 23):
    if 1 <= i <= 8:
        all_urls.append(
            f"https://api.hh.ru/vacancies?date_from=2022-12-19T0{i}:00:00&date_to=2022-12-19T0{i + 1}:00:00&specialization=1&")
    elif i == 9:
        all_urls.append(
            f"https://api.hh.ru/vacancies?date_from=2022-12-19T0{i}:00:00&date_to=2022-12-19T{i + 1}:00:00&specialization=1&")
    else:
        all_urls.append(
            f"https://api.hh.ru/vacancies?date_from=2022-12-19T{i}:00:00&date_to=2022-12-19T{i + 1}:00:00&specialization=1&")

df = pd.DataFrame(columns=["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"])

# Находим количество страниц, идем по каждой странице, берем все вакансии на странице и идём по всем вакансиям
for url in all_urls:
    pages = requests.get(url).json()
    for page in range(pages["pages"]):
        params = {'page': page}
        vacancies_response = requests.get(url, params=params)
        vacancies_json = requests.get(url, params=params).json()
        vacancies_items = vacancies_json["items"]
        for vacancy in vacancies_items:
            try:
                df.loc[len(df)] = [vacancy["name"], vacancy["salary"]["from"], vacancy["salary"]["to"],
                                   vacancy["salary"]["currency"], vacancy["area"]["name"], vacancy["published_at"]]
            except TypeError:
                continue

df.to_csv("Vacancies_by_HH.csv", index=False)
print(df)