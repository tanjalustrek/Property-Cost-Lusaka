# Import needed libraries
import csv
from bs4 import BeautifulSoup
import requests

def find_property():
    # Base URL for properties in Lusaka (capital of Zambia), with a placeholder for the page number
    base_url = 'https://www.property24.co.zm/apartments-flats-for-sale-in-lusaka-c2327?Page={}'

    # Open CSV file for writing data
    with open('property.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Define CSV fieldnames
        fieldnames = ['Price', 'Bedrooms', 'Bathrooms', 'Size']
        # Create CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write CSV header row
        writer.writeheader()

        # Loop through pages 1 to 10
        for page_number in range(1, 11):
            # Construct the URL for the current page
            url = base_url.format(page_number)
            # Send a GET request to the URL
            response = requests.get(url)

            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                # Get the HTML content of the response
                html_text = response.text
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(html_text, 'lxml')
                # Find all property elements on the page
                properties = soup.find_all('span', class_='p24_content')

                # Loop through each property element found
                for property in properties:
                    # Extract price information
                    price_span = property.find('span', class_='p24_price')
                    price = price_span.text.replace(' ', '').strip() if price_span else 'N/A'

                    # Extract bedrooms information
                    bedrooms_span = property.find('span', class_='p24_featureDetails', title='Bedrooms')
                    bedrooms = bedrooms_span.span.text.replace(' ', '').strip() if bedrooms_span else 'N/A'

                    # Extract bathrooms information
                    bathrooms_span = property.find('span', class_='p24_featureDetails', title='Bathrooms')
                    bathrooms = bathrooms_span.span.text.replace(' ', '').strip() if bathrooms_span else 'N/A'

                    # Extract size information
                    size_span = property.find('span', class_='p24_size')
                    size = size_span.span.text.replace(' ', '').strip() if size_span else 'N/A'

                    # Write the property data to the CSV file
                    writer.writerow({'Price': price, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Size': size})
            else:
                # Print error message if fetching page failed
                print(f"Failed to fetch page {page_number}. Status code: {response.status_code}")

# Call the function to start scraping property data
find_property()
