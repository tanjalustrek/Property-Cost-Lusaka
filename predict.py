import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import os

def predict_price(data_full):
    # Extracting the target value
    y = data_full['Price'].to_numpy()

    # Extracting the "raw" feature values
    X = data_full.drop(['Price', 'Source'], axis=1).to_numpy()

    # Feature values with dummy variables for the 'Bathrooms' and 'Bedrooms' columns
    X_dummy = pd.get_dummies(data_full, columns = ['Bathrooms', 'Bedrooms']).drop(['Price', 'Source'], axis=1)
    X_dummy = X_dummy.to_numpy()

    # Feature values where the values of 'Size' column are standardized
    X_stand = data_full.drop(['Price', 'Source'], axis=1)
    X_stand['Size'] = (X_stand['Size'] - np.mean(X_stand['Size']))/(np.std(X_stand['Size']))
    X_stand = X_stand.to_numpy()

    # I create the following two datasets to eliminate the effect of multicollinearity
    # The features are the number of bedrooms and bathrooms
    X_rooms = data_full[['Bedrooms', 'Bathrooms']].to_numpy()

    # The only feature is the size of the apartment/house
    X_size = data_full['Size'].to_numpy()

    # Set random seed for reproducibility
    np.random.seed(7)
    os.environ['LOKY_MAX_CPU_COUNT'] = '4'

    # Initialize KFold object with 5 splits
    kfold = KFold(n_splits=5, shuffle=True)

    # Initialize lists to store errors for each model and each dataset
    lr_errors = {'X': [], 'X_dummy': [], 'X_stand': [], 'X_rooms': [], 'X_size': []}
    knn_errors = {'X': [], 'X_dummy': [], 'X_stand': [], 'X_rooms': [], 'X_size': []}
    rf_errors = {'X': [], 'X_dummy': [], 'X_stand': [], 'X_rooms': [], 'X_size': []}

    datasets = {'X': X, 'X_dummy': X_dummy, 'X_stand': X_stand, 'X_rooms': X_rooms, 'X_size': X_size}

    # Loop through each dataset
    for dataset_name, dataset in datasets.items():

        # Loop through each fold
        for i, (train_index, test_index) in enumerate(kfold.split(dataset)):
            # This if statement deals with the one-dimensionality of the X_size dataset
            if dataset_name == 'X_size':
                # I deal with the one-dimensional X_size dataset by adding an extra dimension
                # Split data into training and testing sets
                x_train = dataset[train_index]
                x_train = x_train[:, None] # Add dimension
                y_train = y[train_index]
                x_test = dataset[test_index]
                x_test = x_test[:, None] # Add dimension
                y_test = y[test_index]

            else:
                # Split data into training and testing sets
                x_train = dataset[train_index, :]
                y_train = y[train_index]
                x_test = dataset[test_index, :]
                y_test = y[test_index]

            # Linear Regression
            lr_model = LinearRegression().fit(x_train, y_train) # Training the model
            y_pred_lr = lr_model.predict(x_test) # Predicting values
            lr_error = np.sqrt(mean_squared_error(y_test, y_pred_lr)) # Computing the RMSE
            lr_errors[dataset_name].append(lr_error)

            # K-Nearest Neighbors Regression
            knn_model = KNeighborsRegressor().fit(x_train, y_train) # Training the model
            y_pred_knn = knn_model.predict(x_test) # Predicting values
            knn_error = np.sqrt(mean_squared_error(y_test, y_pred_knn)) # Computing the RMSE
            knn_errors[dataset_name].append(knn_error)

            # Random Forest Regression
            rf_model = RandomForestRegressor().fit(x_train, y_train) # Training the model
            y_pred_rf = rf_model.predict(x_test) # Predicting values
            rf_error = np.sqrt(mean_squared_error(y_test, y_pred_rf)) # Computing the RMSE
            rf_errors[dataset_name].append(rf_error)
   
    # Print mean RMSE for each model and each dataset
    description = ["Full dataset:", "\nDataset with dummy variables:", "\nDataset with standardised 'Size' column:", "\nDataset without the 'Size' column:", "\nDataset with only the 'Size' column:"]
    for i, dataset_name in enumerate(datasets.keys()):
        print(f"{description[i]}")
        print(f"Mean RMSE Linear Regression: {np.mean(lr_errors[dataset_name])}")
        print(f"Mean RMSE KNN Regression: {np.mean(knn_errors[dataset_name])}")
        print(f"Mean RMSE Random Forest Regression: {np.mean(rf_errors[dataset_name])}")