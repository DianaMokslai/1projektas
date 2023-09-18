from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2


def create_and_insert_product():
    connection = psycopg2.connect(
        host='localhost',
        port=5432,
        database="products",
        user="postgres",
        password="kotiono4ek"
    )


    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS varle_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    quantity INT
    )
"""

    cursor.execute(create_table_query)
# print("Table created successfully")

    url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
    response = requests.get(url)
    # print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    product_elements = soup.find_all('div', class_='GRID_ITEM')
    # print(product_elements)

    product_data = []

    for product_element in product_elements:
        product_name = product_element.find('div', class_='product-title').text.strip()
        product_price = product_element.find('span', class_='price-value').text.strip()[:7]
        product_quantity = product_element.find('b').text.strip()

        # print(f"Adding products to the list: {product_name}")
        product_data.append((product_name, product_price, product_quantity))
        # print('Products inserted into list successfully!')
    connection.commit()
    df = pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
    print(df)

if __name__ == '__main__':
    create_and_insert_product()
