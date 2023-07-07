from bs4 import BeautifulSoup
import requests
url = url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

# it extract the data in a formating form
# print(soup.prettify()[:5000])

title_text = soup.select('title')  # to select the title
title_text[0].getText() # To extract the only data with separator not contain any tag

table_code = soup.find('tbody') # To find the first table body

world_data = table_code.find_all('tr') # To pull the all the tabel tag
# collecting the data
complete_data = []
for i in range(8,len(world_data)):# To extract the row of the data
  data = []
  list_data = world_data[i].find_all('td')
  # print(list_data)
  
  for col in list_data: # # To extract the col of the data
    data.append(col.getText())
  complete_data.append(data)
# print(complete_data[0])

# map the data
maped_data = list(map(lambda x: x[0:10] + [x[12]] + [x[14]],complete_data))
# print(map_data[0])

column_names = [
    '#',
    'country_names',
    'total_cases',
    'new_cases',
    'total_deaths',
    'new_deaths',
    'total_recovered',
    'new_recovered',
    'active_cases',
    'serious_cases',
    'total_tests',
    'population'
]

import csv
filename = 'covid_data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(maped_data)

#import pandas for a Dataframe
import pandas as pd
df = pd.DataFrame(maped_data,columns = column_names)

# save to csv file
df.to_csv('covid_data.csv',index=False)

# read csv file
df_read = pd.read_csv('covid_data.csv')



# Extract the "country_names" and "total_cases" columns
country_names = df['country_names'][0:10]
total_cases = df['total_cases'][0:10]
total_death = df['total_deaths'][0:10]

# data preprocessing
# correct data format replace the seprator "," to ""
df["total_cases"] = df["total_cases"].map(lambda x: int(x.replace(",","")))
# Visualizing the data
import plotly.express as px
from matplotlib import pyplot as plt
# To  present the data in the 
df_plot = df.head(20) # visual+ize the first 20 data
# Create a bar plot using Plotly Express
Bars = px.bar(df_plot, x='country_names', y='total_deaths', 
             labels={'country_names': 'Country', 'total_deaths': 'Total Deaths'},
             title='COVID-19 Total Cases by Country')

print(Bars.show())


