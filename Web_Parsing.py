import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint
file = open('books.csv', 'w', encoding='utf-8_sig', newline='\n')
write_obj = csv.writer(file)
write_obj.writerow(['Title', 'Author', 'Link'])
ind = 1


while ind < 2:
    url = f'https://www.lit.ge/index.php?page=books&send[shop.catalog][page]=4'
    response = requests.get(url)
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    book_section = soup.find('section', class_='list-holder')
    all_books = book_section.find_all('article')
    for book in all_books:
        img_address = book.img.attrs.get('src')
        right = book.find('div', class_='span10')
        title = right.a.text
        author = right.b.a.text
        write_obj.writerow([title, author, img_address])
        print(title,author)
    ind += 1
    print(ind, response.url)
    time.sleep(randint(1, 7))

import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

# Open the CSV file for writing
file = open('phones.csv', 'w', encoding='utf-8_sig', newline='\n')
write_obj = csv.writer(file)
write_obj.writerow(['Name', 'Price', 'Link'])

ind = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

while ind < 2:
    url = f'https://be.ge/ge/products/mobiluri-telefonebi-500?page={ind}&limit=24'
    response = requests.get(url, headers=headers)
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    product_section = soup.find('div', class_='products')
    all_products = product_section.find_all('div')
    for product in all_products:
        below = product.find('div', href_)


        if product_section:
            for product in product_section:
                name = product.find('div', class_='product-box--name').text.strip()
                price = product.find('div', class_='product-box--price').text.strip()
                link = product.find('a', class_='product-box--name-link')['href']
                write_obj.writerow([name, price, link])
                print(f'Scraped: {name} - {price} - {link}')
        else:
            print(f'No product section found on page {page_index}')
    else:
        print(f'Failed to fetch page {page_index}')

    # Increment the page index
    page_index += 1
    print(f'Completed scraping page {page_index - 1}')

    # Delay to avoid overloading the server
    time.sleep(randint(15, 20))

# Close the CSV file
file.close()
print('Scraping complete. Data saved to phones.csv')
