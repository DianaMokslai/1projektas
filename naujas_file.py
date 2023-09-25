from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import time
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns

#
# #
# # Apskaičiuokite kiekvieno produkto mėnesinį pardavimų sumažėjimą per metus.
# # Sukurkite Matplotlib grafiką, kuriame būtų pateikti šie mėnesiniai sumažėjimai kiekvienam produktui (x ašis - mėnesiai, y ašis - sumažėjimas, produkto pavadinimas - linijos pavadinimas).
# # Pridėkite pavadinimus ašims ir bendrą pavadinimą grafikui.
#
# df = pd.read_csv('prekybos_duomenys.csv')
# print(df.head(5))
# df['Data'] = pd.to_datetime(df['Data'])
# df['Metai'] = df['Data'].dt.year
# df['Mėnuo'] = df['Data'].dt.month
# df['Diena'] = df['Data'].dt.day
# # print(f'\n', df)
# pagal_produkta = df.groupby(['Mėnuo','Produktas']) ['Pardavimai'].sum()
# products = df['Produktas']
# result = pd.DataFrame(columns=['Produktas', 'Metai', 'Mėnuo', 'Sumazejimas'])
# for product in products:
#     product_df=df[df['Produktas']== product]
#     for year in product_df['Metai'].unique():
#         for month in range(1,13):
#             if product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)].shape[0]>0:
#                 sales = product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)]['Pardavimai'].sum()
#                 if month >1:
#                     praeje_metai=year
#                     peaejes_men=month-1
#                 else:
#                     praeje_metai = year-1
#                     peaejes_men = 12
#                 pr_sales=\
#                 product_df[(product_df['Metai']==praeje_metai) & (product_df['Mėnuo']== peaejes_men)]['Pardavimai'].sum()
#                 decrease = pr_sales-sales
#                 result = pd.concat([result,pd.DataFrame([[product,year,month,decrease]],columns=result.columns)],ignore_index=True)
# print(result)
#
#
# plt.plot(result ['Produktas'], result['Sumazejimas'], label = 'linija', color='blue', linestyle='--', marker = 'o')
#
#
# plt.xlabel('Menuo')
# plt.ylabel('sumazejimas')
# plt.title('Pardavimu mazejimas')
# plt.xticks(rotation=90)
# plt.show()

# Išspausdinkite pirmas 5 eilutes;
# Filtruokite automobilius pagal jų kainą (pvz., kaina mažesnė nei 10 000). Išspausdinkite šiuos automobilius;
# Suskirstykite automobilius pagal gamintoją ir susumuokite kiekvieno gamintojo automobilių kiekius.
# Atvaizduokite stulpelinėje diagramoje automobilių kiekius;


# df = pd.read_csv('automobiliai.csv')
# print(df.head(5))
# filtravimas = df[df['Kaina']>10000]
# print(filtravimas)
#
# pagal_gamintoja = df['Markė'].value_counts()
# print((pagal_gamintoja))
#
# pagal_gamintoja.plot(kind='bar', color='green')
# plt.show()

# URL: https://coinmarketcap.com
#
# Naudokite Beautiful Soup, kad galėtumėte „web scraping
# " funkcionalumą, kad gautumėte kriptovaliutos kainų duomenis iš populiarios kriptovaliutų rinkos svetainės.
# Išgaukite kainų, laiko ir kitus susijusius duomenis iš svetainės.
#
# Įkelkite gautus duomenis į Pandas DataFrame.
# Atliekant duomenų tvarkymą, galite konvertuoti datą
# į tinkamą formatą, ištrinti dublikatus arba tvarkyti trūkstamas reikšmes.
#
# Atlikite analizę, kad gautumėte statistiką apie kriptovaliutos kainų kitimą.
# Paskaičiuokite vidutines, minimalias ir maksimalias kainas, taip pat kitas statistikos vertes.
#
# Sukurkite linijinį grafiką, kuris atvaizduoja
# kriptovaliutos kainos kitimą laike (x ašis - laikas, y ašis - kaina).
#
#Taip pat galite sukurti stulpelinį grafiką, kuris rodo kainos svyravimus tarp skirtingų kriptovaliutų.

#
# funkcionalumą, kad gautumėte kriptovaliutos kainų duomenis iš populiarios kriptovaliutų rinkos svetainės.
# # Išgaukite kainų, laiko ir kitus susijusius duomenis iš svetainės.
#
# url = 'https://coinmarketcap.com'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
# crypto = soup.find_all('div', class_='grid')
# print(crypto)
#
# header = ['Column1', 'Column2', 'Column3']
# manoduomenis = pd.DataFrame(columns=header)
#
#
# for i in crypto[0].find_all('tr')[1:]:
#         row_data = find_all('td')
#         row_values =  [data.text for data in row_data]
#         # length = len(mydata)
#         manoduomenis.loc[len(manoduomenis)] = row_values
# print(manoduomenis)

# for i in range (1,4):
#         print('Puslapis {0}'.format(i))
#         params = {
#                 'page':1
#
#         }
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         tableble.append(pr.read_htm(str(soup))[0])
#
# naujas _tabel = pd.concat(table)
# naujas_table.loc[:,naujas_table.columns[1:-1]]
# naujas_table.csv('Crypto.csv', index = False)


# #
# for product_element in product_elements:
# Crypto_name = product_element.find('div', class_='sc-aef7b723-0 sc-efbac737-1 bZnFXd  hide-ranking-number').text.strip()
# Crypto_price = float(product_element.find('span', class_='sc-a0353bbc-0 gDrtaY').text.strip().replace('€', ''))
#
# print(product_name,product_price)
# d = {
#
#
# d = {
#         'datetime': [i[0] for i in r.json()['prices']],
#         'price': [i[1] for i in r.json()['prices']]
# }
#
#
# url = 'https://coinmarketcap.com'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# table = soup.find('table')
# # headers = [header.text.strip() for header in table.find_all('th')]
# # print(crypto)
#
# df = pd.DataFrame(columns=headers)
#
# rows = table.find('tbody').find_all('tr')
#
# for row in rows:
#     row_data = [data.text.strip() for data in row.find_all('td')]
#     df.loc[len(df)] = row_data
#
# print(df)
#
# table = []
#
# for i in headers:
#     table = i.text
# #     tables.append(table)
# print(tables)
#
# df = pd.DataFrame(columns = tables)
# print(df)
#
# row = table.find_all('tr')
# # print(row)
#
#
# url = 'https://coinmarketcap.com'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
# Crypto = soup.find_all('div', class_='grid')
# print(Crypto)
#
# table = soup.select('sc-aef7b723-0 dGuXpm table-link-area')[0]
# columns = table.find_all('th')
# columns
#
# table_df = pd.read_html(str(table))[0]
#
# table_df
# # table = []
#
# for i in range(1):
#     duomenys = {
#         'page': 1
#     }
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

url = 'https://coinmarketcap.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []
table = soup.find('table', attrs={'class':'cmc-table'})
cols = table.find('thead').find_all('th')
cols = [ele.text.strip() for ele in cols]
data.append([ele for ele in cols if ele])

lentele = table.find('tbody')

# print(lentele)

rows = lentele.find_all('tr')
for row in rows:
    cols = row.find_all('td')

    # print(cols)
    colsTemp = []

    for i, col in enumerate(cols):
        if i == 2 and len(col.findAll('p')) > 1:
            colsTemp.append(col.findAll('p')[0].text + " " + col.findAll('p')[1].text) # formatuojam teksta
        elif i == 7 and len(col.findAll('span')) > 0: #grazinam reiksme
            span = col.findAll('span')
            colsTemp.append(span[1].text if len(span) > 1 else span[0].text)
        else:
            colsTemp.append(col.text.strip())

    cols = colsTemp
    data.append([ele for ele in cols if ele]) # Get rid of empty values

df = pd.DataFrame(data)

print(df.head(n=15))

df.to_csv('Crypto.csv', index=False)

df = pd.read_csv('Crypto.csv')



