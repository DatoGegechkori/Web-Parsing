import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

with open('TVs.csv', 'w', encoding='utf-8_sig', newline='\n') as file:
    write_obj = csv.writer(file)
    write_obj.writerow(['Title', 'Price', 'Link'])

    ind = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'
    }

    while ind < 5:
        url = f'https://isurve.ge/collections/televizorebi?page={ind}'
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all_products = soup.find_all('div', class_='grid-view-item')

        for product in all_products:
            title = product.find('div', class_='h4 grid-view-item__title').text
            price = product.find('span', class_='product-price__price').text
            img_tag = product.find('img')

            if img_tag:
                link = img_tag.attrs.get('src', 'No image link')

                write_obj.writerow([title, price, link])
                print(title, price, link)

        ind += 1
        print(f"Page {ind}")
        duration = randint(7, 15)
        print(f'Sleeping for {duration} seconds')
        time.sleep(duration)


