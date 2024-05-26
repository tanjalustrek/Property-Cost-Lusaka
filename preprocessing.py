import pandas as pd
import numpy as np
from data import find_property 
from exchange_rate import fetch_eur_exchange_rate

# The purpose of this function is to prep the fetched data to ensure it's ready for detailed analysis later on
def preprocess_data():
    # Import apartments data fetched from Property24
    find_property() # This line takes quite a bit of time as there is a lot of data to get through
    data = pd.read_csv('property.csv')

    # Get the current exchange rate
    exchange_rate = fetch_eur_exchange_rate()

    # Convert 'Price' to numeric and change to €
    data['Price'] = data['Price'].str.extract('(\d+)').astype(float)
    data['Price'] = data['Price'] * float(exchange_rate)

    # Define a function to extract the size value in m²
    def size_cleared(value):
        if isinstance(value, (float, int)):
            return float(value)
        elif 'm²' in value:
            return float(value.replace('m²', '').strip())
        elif 'acres' in value:
            acres = float(value.replace('acres', '').strip())
            return acres * 4046.86
        else:
            return np.nan

    data['Size'] = data['Size'].apply(size_cleared)

    # Calculate the mean and standard deviation for each column
    mean = data.mean()
    std = data.std()

    # Removing outliers based on
    # 'Price'
    data = data[abs(data['Price'] - mean[0]) <= 1 * std[0]]

    # 'Size'
    data = data[(np.isnan(data['Size'])) | (abs(data['Size'] - mean[3]) <= 1 * std[3])]

    # 'Bathrooms' and 'Bedrooms'
    data = data[((np.isnan(data['Bathrooms'])) | (abs(data['Bathrooms'] - mean[2]) <= 2 * std[2])) &
                ((np.isnan(data['Bedrooms'])) | (abs(data['Bedrooms'] - mean[1]) <= 2 * std[1]))]

    # Replace the NaN values in 'Bedrooms' and 'Bathrooms' with their respective modes
    mode_bedrooms = data['Bedrooms'].mode()[0]
    data['Bedrooms'] = data['Bedrooms'].fillna(mode_bedrooms)

    mode_bathrooms = data['Bathrooms'].mode()[0]
    data['Bathrooms'] = data['Bathrooms'].fillna(mode_bathrooms)

    return data