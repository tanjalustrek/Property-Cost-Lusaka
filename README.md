# Property Cost Lusaka

This repository contains code for scraping information about properties being sold in Cape Town and building machine learning models to predict property prices based on the collected data.

## Data Collection
The data collection process involves scraping property listings in Cape Town from the real estate website [Propery24](https://www.property24.com/). I extracted information such as property size, price, number of bedrooms and bathrooms.

## Data Preprocessing
Once I have the raw data, I perform data preprocessing steps to clean and prepare the data for analysis. This includes handling missing values, encoding categorical variables, scaling numerical features, and any other necessary transformations.

## Machine Learning Models
I develop machine learning models to predict property prices based on the collected data. The models are trained using regression algorithms (linear, random forest and k-nearest neighbors regression).

## Repository Structure
- `data.py`: Contains the function used to scrape the data.
- `exchange_rate.py`: Contains the function used to get the current exchange rate from South African Rand (ZAR) to Euro (EUR).
- `preprocessing.py`: Contains the function used to preprocess the data.
- `propery.csv`: The CSV file created by running the function in the `preprocessing.py` file.
- `size.py`: Contains the function used to predict and fill the mising size values.
- `predict.py`: Contains the function used for model training and evaluation.
- `predict_your_price.py`: Contains the function used to predict the property value based on given parameters.
- `analysis.ipynb`: Jupyter notebook used to display the results.
- `README.md`: You're reading it right now!

## Usage
To view the results generated on 7/5/2024, simply open the `analysis.ipynb` file in your preferred Jupyter notebook environment.

If you wish to reproduce the analysis or run the code with updated data, clone or download this repository to your local machine and run the `analysis.ipynb` file in your Jupyter notebook environment to execute the analysis and view the results (make sure you have Python installed along with other necessary dependencies). Be aware that the data fetching will take quite a long time as there is a lot of data to get through.

Please note that your results may vary depending on the data available at the time of execution.