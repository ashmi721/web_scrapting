import sqlite3
import pandas as pd
# create a database  connection with the sqlite3
conn = sqlite3.connect('covide_data.db')
cur = conn.cursor()
# print(cur)

# create a table 
# cur.execute(''' CREATE TABLE covid_state(
#              ID             INT           PRIMARY KEY           NOT NULL,
#              NAMES          VARCHAR(50)                         NOT NULL,
#              TOTALCASES     VARCHAR(50)                        NOT NULL,
#              TOTALDEATHS     VARCHAR(50),
#              TOTALRECOVERED  VARCHAR(50),
#              TOTALTESTS      VARCHAR(50)
#             )''')

# Read the CSV file into a DataFrame
df = pd.read_csv('covid_data.csv')
df_store = df.head() # extract the first 5 rows

# Select the desired columns from the DataFrame
selected_columns = ['#','country_names', 'total_cases', 'total_deaths', 'total_recovered', 'total_tests']
df_selected = df_store[selected_columns]

# Iterate over the selected DataFrame and insert the data into the table
for idx, row in df_selected.iterrows():
    country_names = row['country_names']
    total_cases = row['total_cases']
    total_deaths = row['total_deaths']
    total_recovered = row['total_recovered']
    total_tests = row['total_tests']

    try:
        # Insert the data into the table
        conn.execute(f'''INSERT INTO covid_state (ID, NAMES, TOTALCASES, TOTALDEATHS, TOTALRECOVERED, TOTALTESTS)
                         VALUES (?,?,?,?,?,?)''',(country_names,total_cases,total_deaths,total_recovered,total_tests))
    
    except Exception as e:
        print(f'{row} already inserted')

    else:
        conn.commit()


    # select the data 
# cur.execute('''SELECT * FROM covid_state''')
# results= cur.fetchall()
# print(results)
# conn.commit()