# Property Cost Lusaka

This repository contains code for scraping information about properties being sold in Lusaka and building machine learning models to predict property prices based on the collected data.

## Data Collection
The data collection process involves scraping property listings in Lusaka from the real estate website [Propery24](https://www.property24.com/). I extracted information such as property size, price, number of bedrooms and bathrooms.

## Data Preprocessing
Once I have the raw data, I perform data preprocessing steps to clean and prepare the data for analysis. This includes handling missing values, encoding categorical variables, scaling numerical features, and any other necessary transformations.

## Machine Learning Models
I develop machine learning models to predict property prices based on the collected data. The models are trained using regression algorithms (linear, random forest and k-nearest neighbors regression).

## Repository Structure
- `data.py`: Contains the function used to scrape the data.
- `propery.csv`: The CSV file created by running the `data.py` file.
- `exchange_rate.py`: Contains the function used to get the current exchange rate from ZMW to EUR.
- `analysis.ipynb`: Jupyter notebook used for preprocessing and model building.
- `README.md`: You're reading it right now!

## Usage
To view the results generated on 7/5/2024, simply open the `analysis.ipynb` file in your preferred Jupyter notebook environment.

If you wish to reproduce the analysis or run the code with updated data, clone or download this repository to your local machine and run the `analysis.ipynb` file in your Jupyter notebook environment to execute the analysis and view the results (make sure you have Python installed along with other necessary dependencies).

Please note that your results may vary depending on the data available at the time of execution.