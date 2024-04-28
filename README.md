# Propert Cost Lusaka

This repository contains code for scraping information about properties being sold in Lusaka and building machine learning models to predict property prices based on the collected data.

## Data Collection
The data collection process involves scraping property listings in Lusaka from the real estate website [Propery24](https://www.property24.com/). I extracted information such as property size, price, number of bedrooms and bathrooms.

## Data Preprocessing
Once I have the raw data, I perform data preprocessing steps to clean and prepare the data for analysis. This includes handling missing values, encoding categorical variables, scaling numerical features, and any other necessary transformations.

## Machine Learning Models
I develop machine learning models to predict property prices based on the collected data. The models are trained using regression algorithms (linear, random forests and k-nearest neighbors regression).

## Repository Structure
- `data.py`: Contains the function used to scrape the data.
- `propery.csv`: The CSV file created by running the `data.py` file.
- `analysis.ipynb`: Jupyter notebook used for preprocessing and model building.
- `README.md`: You're reading it right now!

## Usage
If you just want to se the results, you can check the `analysis.ipynb` file, which contains the results of the data that was scraped on 28/4/2024. Otherwise, first run the `data.py` file and then the `analysis.ipynb` file, where all the results will print out (your results will like be different from mine since property listings will probabli change).