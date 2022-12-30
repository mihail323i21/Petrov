# import math
# import sqlite3
# from statistics import mean
# import pandas as pd
#
#
# def sort_area_dict(dictionary):
#     sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:10]
#     sorted_dict = {k: v for k, v in sorted_tuples}
#     return sorted_dict
#
#
# print("Используемая база данных: new_vac_with_dif_currencies.db")
# vac = input("Введите название профессии: ")
# vac = f"%{vac}%"
# con = sqlite3.connect("new_vac_with_dif_currencies.db")
# cur = con.cursor()
# database_length = pd.read_sql("SELECT COUNT(*) From new_vac_with_dif_currencies", con).to_dict()["COUNT(*)"][0]
#
# # Динамика уровня зарплат по годам
# s_groups_by_y = pd.read_sql("SELECT years, ROUND(AVG(salary)) From new_vac_with_dif_currencies GROUP BY years", con)
# salaries_by_year = dict(s_groups_by_y[["years", "ROUND(AVG(salary))"]].to_dict("split")["data"])
#
# # Динамика количества вакансий по годам
# v_groups_by_y = pd.read_sql("SELECT years, COUNT(name) From new_vac_with_dif_currencies GROUP BY years", con)
# vacancies_by_year = dict(v_groups_by_y[["years", "COUNT(name)"]].to_dict("split")["data"])
#
# # Динамика уровня зарплат по годам для выбранной профессии
# i_v_s_groups_by_y = pd.read_sql("SELECT years, ROUND(AVG(salary)) From new_vac_with_dif_currencies "
#                                 "WHERE name LIKE :vac "
#                                 "GROUP BY years", con, params=[vac])
# inp_vacancy_salary = dict(i_v_s_groups_by_y[["years", "ROUND(AVG(salary))"]].to_dict("split")["data"])
#
# # Динамика количества вакансий по годам для выбранной профессии
# i_v_c_groups_by_y = pd.read_sql("SELECT years, COUNT(name) From new_vac_with_dif_currencies "
#                                 "WHERE name LIKE :vac "
#                                 "GROUP BY years", con, params=[vac])
# inp_vacancy_count = dict(i_v_c_groups_by_y[["years", "COUNT(name)"]].to_dict("split")["data"])
#
# # Уровень зарплат по городам (в порядке убывания)
# s_a_groups_by_c = pd.read_sql("SELECT area_name, ROUND(AVG(salary)), COUNT(area_name) From new_vac_with_dif_currencies "
#                               "GROUP BY area_name "
#                               "ORDER BY COUNT(area_name) DESC ", con)
#
# s_a_groups_by_c = s_a_groups_by_c[s_a_groups_by_c["COUNT(area_name)"] >= 0.01 * database_length]
# salaries_areas = dict(s_a_groups_by_c[["area_name", "ROUND(AVG(salary))"]].to_dict("split")["data"])
# salaries_areas = sort_area_dict(salaries_areas)
#
# # Доля вакансий по городам (в порядке убывания)
# v_a_groups_by_c = pd.read_sql("SELECT area_name, COUNT(area_name) From new_vac_with_dif_currencies "
#                               "GROUP BY area_name "
#                               "ORDER BY COUNT(area_name) DESC "
#                               "LIMIT 10", con)
# v_a_groups_by_c["COUNT(area_name)"] = round(v_a_groups_by_c["COUNT(area_name)"] / database_length * 100, 2)
# vacancies_areas = dict(v_a_groups_by_c[["area_name", 'COUNT(area_name)']].to_dict("split")["data"])
#
# print("Динамика уровня зарплат по годам:", salaries_by_year)
# print("Динамика количества вакансий по годам:", vacancies_by_year)
# print("Динамика уровня зарплат по годам для выбранной профессии:", inp_vacancy_salary)
# print("Динамика количества вакансий по годам для выбранной профессии:", inp_vacancy_count)
# print("Уровень зарплат по городам (в порядке убывания):", salaries_areas)
# print("Доля вакансий по городам (в порядке убывания):", vacancies_areas)
