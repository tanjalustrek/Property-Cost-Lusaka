import requests
from bs4 import BeautifulSoup

def fetch_eur_exchange_rate():
    # Define the URL for currency conversion
    url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=ZMW'

    # Send a GET request to fetch the HTML content
    html_text = requests.get(url)

    # Check if the request was successful (status code 200)
    if html_text.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(html_text.text, 'html.parser')
        
        # Find the specific div containing the exchange rate value
        div_element = soup.find('div', class_='sc-ac62c6d1-0 GwlFu')
        
        # Check if the div element is found
        if div_element:
            # Find the <p> tag within the div that contains the exchange rate value
            exchange_rate_value = div_element.find('p')
            
            # Check if the exchange rate value is found
            if exchange_rate_value:
                # Split the exchange rate information by the equals sign
                parts = exchange_rate_value.text.split('=')
                
                # Extract the EUR value from the second part and remove leading/trailing whitespace
                eur_value = parts[1].strip().split()[0]  # Get the first token after splitting by whitespace
                
                # Return the extracted EUR value
                return float(eur_value)
            else:
                print("Exchange rate value not found.")
        else:
            print("Div element not found.")
    else:
        print("Failed to fetch URL:", url)
    return None