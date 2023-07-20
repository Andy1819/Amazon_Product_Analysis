import csv
from bs4 import BeautifulSoup

with open('./Webscrapping/index1.html', 'r',encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

div_elements = soup.find_all('div', class_='sg-col-inner')

scraped_data = []

for div in div_elements:
    brand = div.find('span', class_='a-size-base-plus a-color-base')
    brand = brand.text if brand else ''

    title = div.find('span', class_='a-size-base-plus a-color-base a-text-normal')
    title = title.text if title else ''

    rating = div.find('span', class_='a-icon-alt')
    rating = rating.text if rating else ''

    price = div.find('span', class_='a-price-whole')
    price = price.text if price else ''

    scraped_data.append([brand, title, rating, price])

with open('./datasets/data_shirts.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Brand', 'Title', 'Rating', 'Price'])
    writer.writerows(scraped_data)

print("Scraping completed. Data saved in 'data.csv'.")
