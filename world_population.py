import requests
from bs4 import BeautifulSoup
url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
# To extract the table data
rows = soup.find('table',{'id':'example2'}).find('tbody').find_all('tr')

countries_list = []
for row in rows:
   dic = {} 
   dic['#'] = row.find_all('td')[0].text
   dic['Country'] = row.find_all('td')[1].text # to extract the country name
   dic['Population 2023'] = row.find_all('td')[2].text.replace(',','')
   dic['Land Area(km^2)'] = row.find_all('td')[6].text.replace(',','')
   dic['Migrants(net)'] = row.find_all('td')[7].text.replace(',','')
  
  
   countries_list.append(dic)

import pandas as pd
df = pd.DataFrame(countries_list)

df.to_csv('countries_data.csv', index=False) # to save the data in csv file
pd.read_csv('countries_data.csv')
# df.to_excel('countries_data.xlsx') # to save the data in the excel

df_plot = df.head(10)

# extract the country_name and population column
country_name = df_plot['Country']
population = df_plot['Population 2023'] 

import plotly.express as px

fig = px.bar(x=country_name, y=population)
fig.update_layout(title="Population in 2023 by Country")
fig.update_xaxes(title_text="Country")
fig.update_yaxes(title_text="Population 2023")

print(fig.show())