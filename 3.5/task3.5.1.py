# import pandas as pd
# import sqlite3
#
# df = pd.read_csv("CB_Currency.csv")
#
# con = sqlite3.connect("CB_Currency.db")
# cur = con.cursor()
# df.to_sql(name="CB_Currency", con=con, if_exists='replace', index=False)
# con.commit()
