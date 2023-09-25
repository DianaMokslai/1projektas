from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import time
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host='localhost',
#         port=5432,
#         database="products",
#         user="postgres",
#         password="kotiono4ek"
#     )
#
#
#     cursor = connection.cursor()
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS varle_products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     price DECIMAL(10,2),
#     quantity INT
#     )
# """
#
#     cursor.execute(create_table_query)
# print("Table created successfully")
#
#
# url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
# #
# #
# response = requests.get(url)
#     # print(response.status_code)
# #
# soup = BeautifulSoup(response.content, 'html.parser')
#
# product_elements = soup.find_all('div', class_='GRID_ITEM')
# print(product_elements)
#
#     product_data = []
# #
#     for product_element in product_elements:
#         product_name = product_element.find('div', class_='product-title').text.strip()
#         product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
#         product_quantity = product_element.find('b').text.strip()[:1]

#         print(f"Adding products to the list: {product_name}")
#         time.sleep(2)
#         # # product_data.append((product_name, product_price, product_quantity))
#         # insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
#         # cursor.execute(insert_query,(product_name, product_price, product_quantity))
#
#         # print('Products inserted into list successfully!')
#         connection.commit()
#
#     # df = pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
#     # print(df)
#     select_query = "SELECT * FROM varle_products"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df = pd.DataFrame(rows, columns=['id', 'name', 'price', 'quantity'])
#     print(df)
#
# if __name__ == '__main__':
#     create_and_insert_product()



# url = 'https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/LT/Hourly/?view=table'
# response = requests.get(url)
# print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# product_elements = soup.find_all('div', class_="ng-scope")
# print(product_elements)

#
# product_data = []
# for product_element in product_elements:
#     product_name = product_element.find('div', class_='row-name').text.strip()
#     # product_price =product_element.find('tr', class_='data-row').text.strip()
#     # product_quantity = product_element.find('a').text.strip()


# url = 'https://www.rde.lt/categories/lt/388/sort/5/filter/0_0_0_0/page/1/Mobilieji-telefonai.html'
# response = requests.get(url)
# # print(response.status_code)
# #
# soup = BeautifulSoup(response.content, 'html.parser')
#
# product_elements = soup.find_all('div', class_="retailrocket-item")
# # print(product_elements)
#
# #
# product_data = []
#
# for product_element in product_elements:
#     product_name = product_element.find('div', class_='retailrocket-item_title').text.strip()
#     product_price = float(product_element.find('span', class_='retailrocket-item_price_value').text.strip().replace('€', ''))
#
#     print(f"Adding products to the list: {product_name}")
#     product_data.append((product_name, product_price))
#
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host = "localhost",
#         port=5432,
#         database = "products",
#         user='postgres',
#         password = "Kaunas2?"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS varle_products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(500),
#     price DECIMAL(10,2),
#     quantity INT)
#     """
#     cursor.execute(create_table_query)
#     print("Table is created successfully!")
#     for i in range(1,125):
#         url = f'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/?p={i}'
#         response = requests.get(url)
#         # print(response.status_code)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         product_elements = soup.find_all('div', class_ = 'GRID_ITEM')
#         # print(product_elements)
#         product_data = []
#         for product_element in product_elements:
#             product_name = product_element.find('div', class_ = 'product-title').text.strip()
#             product_price = float(product_element.find('span', class_ = 'price-value').text.strip().replace('€', ''))
#             product_quantity = product_element.find('b').text.strip()[:1]
#             print(f'Adding products to the list: {product_name}')
#             # time.sleep(2) ## nei b8tina nei privaloma
#             # product_data.append((product_name, product_price, product_quantity))
#             # insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s )"
#             # cursor.execute(insert_query, (product_name, product_price, product_quantity))
#             # print("Products inserted into list successfully!")
#             connection.commit()
#             # df = pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
#             # print(df)
#             # df.to_excel('kompa.xlsx')
#         select_query = "SELECT * FROM varle_products"
#         cursor.execute(select_query)
#         rows = cursor.fetchall()
#         df = pd.DataFrame(rows, columns = ['id', 'name', 'price', 'quantity'])
#         print(df)
# if __name__ == '__main__':
#     create_and_insert_product()
# #
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="ZaislaiProducts",
#         user="postgres",
#         password="Dek***123*"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS zaislai_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2)
#         )
#     """
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#     url = 'https://www.1a.lt/c/zaislu-pasaulis-20-zaislams-su-kodu/87w'
#     response = requests.get(url)
#     print(response.status_code)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_elements = soup.find_all('div', class_='catalog-taxons-products-container__grid-row')
#     # print(product_elements)
#     product_data = []
#     for product_element in product_elements:
#         product_name = product_element.find('div', class_='catalog-taxons-product__files').text.strip()
#         product_price = float(product_element.find('span', class_='catalog-taxons-product-price__item-price').text.strip().replace('€', '').replace('vnt.', '').replace('\n\n/', '').replace(' ','').replace(',', '.'))
#         print(f'Pridedame produktus i sarasa: {product_name}')
#         product_data.append((product_name, product_price))
#         insert_query = "INSERT INTO zaislai_products (name, price) VALUES(%s, %s)"
#         cursor.execute(insert_query, (product_name, product_price))
#         print(f'Products inserted into list succesfully!')
#         connection.commit()
#     # df=pd.DataFrame(product_data, columns=['name', 'price'])
#     # print(df)
#     select_query = "SELECT * FROM zaislai_products"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df=pd.DataFrame(rows, columns = ['id', 'name', 'price'])
#     print(df)
# if __name__ =='__main__':
#     create_and_insert_product()


#
# url = 'http://www.meteo.lt/en/miestas?placeCode=Vilnius'
# response = requests.get(url)
# print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# forecast = soup.find_all('div', class_='forecast-day')
# week_days = soup.find_all('span', class_='date')
# day_temperature = soup.find_all('span', class_='big up-from-zero')[1::2]
# # print(week_days, day_temperature)
# filtered_week_days = [week_day.get_text().split(",")[0] for week_day in week_days]
# day_temperatures = []
# for temperature in day_temperature:
#     temp_text = temperature.get_text().replace('°C', '')
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# print(day_temperatures)
#
# data = {'weekday': filtered_week_days, "temperature": day_temperatures}
# df =pd.DataFrame(data)
# print(df)
# max_temperature = df['temperature'].max()
# print(max_temperature)
#
#
# min_temperature = df['temperature'].min()
# print(min_temperature)
#
# vidurkis = df['temperature'].mean()
# print(vidurkis)
#
# plt.figure(figsize=(12,5))
# plt.bar('auksciausia temperatura', max_temperature, color="green")
# plt.bar('zemiausia temperatura', min_temperature, color="red")
# plt.bar('Vidurkis', vidurkis, color='blue')
# plt.title('Auksciausia ir zemiausia temperatura Vilniuje')
# plt.show()

# # duomenu rinkinys su proc ir pav
#
# proc = [90, 10, 45, 60, 70]
# pasiekimai = ['matematika', 'istorija', 'fizika', 'anglu', 'biologija']
#
# spalvos = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
# ex = (0.1, 0, 0, 0, 0)
#
# # # kiek skaiciu po kableliu = tai reiskia vienas
# fontas = FontProperties(family="Arial", size=14, weight='bold')
# plt.pie(proc, explode=ex, labels=pasiekimai, colors=spalvos, autopct='%1.1f%%', startangle=140)
# plt.title('Pasiekimu diagrama')
# plt.axis('equal')
# plt.show()


data = pd.read_csv('sales_data.csv')
df = pd.DataFrame(data)
print(df)
Crypto = soup.find_all('div', class_='grid')
print(Crypto)
data = {'Stulpelis1_id':[i+1 for i in range(50)],
        'Vardas':[random.choice(['Petka','Vetka','Nulis'])for _ in range(50)],
#         'Alga':[random.randint(1000,1500) for _ in range(50)]
#
# }
# df = pd.DataFrame(data)
# df.to_csv('Atlyginimai.csv', index = False)
















