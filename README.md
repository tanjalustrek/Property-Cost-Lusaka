# Propert Cost Lusaka

This repository contains code for scraping information about properties being sold in Lusaka and building machine learning models to predict property prices based on the collected data.

## Data Collection
The data collection process involves scraping property listings in Lusaka from the real estate website [propery24](https://www.property24.com/). We extract information such as property size, price, number of bedrooms and bathrooms.

## Data Preprocessing
Once we have the raw data, we perform data preprocessing steps to clean and prepare the data for analysis. This includes handling missing values, encoding categorical variables, scaling numerical features, and any other necessary transformations.

## Machine Learning Models
We develop machine learning models to predict property prices based on the collected data. The models are trained using regression algorithms (linear, random forests and k-nearest neighbors regression).

## Repository Structure
- `data.py/`: Contains the function used to scrape the data.
- `