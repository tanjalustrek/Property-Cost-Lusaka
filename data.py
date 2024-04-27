import csv
from bs4 import BeautifulSoup
import requests

def find_apartments():
    base_url = 'https://www.property24.co.zm/apartments-flats-for-sale-in-lusaka-c2327?Page={}'

    with open('apartments.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Price', 'Bedrooms', 'Bathrooms', 'Size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for page_number in range(1, 11):
            url = base_url.format(page_number)
            response = requests.get(url)

            if response.status_code == 200:
                html_text = response.text
                soup = BeautifulSoup(html_text, 'lxml')
                apartments = soup.find_all('span', class_='p24_content')

                for apartment in apartments:
                    price_span = apartment.find('span', class_='p24_price')
                    price = price_span.text.replace(' ', '').strip() if price_span else 'N/A'

                    bedrooms_span = apartment.find('span', class_='p24_featureDetails', title='Bedrooms')
                    bedrooms = bedrooms_span.span.text.replace(' ', '').strip() if bedrooms_span else 'N/A'

                    bathrooms_span = apartment.find('span', class_='p24_featureDetails', title='Bathrooms')
                    bathrooms = bathrooms_span.span.text.replace(' ', '').strip() if bathrooms_span else 'N/A'

                    size_span = apartment.find('span', class_='p24_size')
                    size = size_span.span.text.replace(' ', '').strip() if size_span else 'N/A'

                    writer.writerow({'Price': price, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Size': size})
            else:
                print(f"Failed to fetch page {page_number}. Status code: {response.status_code}")

find_apartments()
