import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import os

def predict_your_price(data, size, bathrooms, bedrooms):
    # Input validation
    if not isinstance(size, (int, float)) or not isinstance(bathrooms, int) or not isinstance(bedrooms, int):
        raise ValueError("Invalid input types. Size must be numeric and bathrooms/bedrooms must be integers.")

    # Prepare data
    y = data['Price'].to_numpy()
    X_stand = data.drop(['Price', 'Source'], axis=1)
    mean = np.mean(X_stand['Size'])
    std = np.std(X_stand['Size'])
    X_stand['Size'] = (X_stand['Size'] - mean) / std
    X_stand = X_stand.to_numpy()

    # Preprocess input data
    size = (size - mean) / std
    values = np.array([bedrooms, bathrooms, size])

    # Initialize models
    lr_model = LinearRegression()
    knn_model = KNeighborsRegressor()
    rf_model = RandomForestRegressor()

    # Initialize lists to store predictions for each model
    lr_predictions = []
    knn_predictions = []
    rf_predictions = []

    # Initialize KFold object with 5 splits
    kfold = KFold(n_splits=5, shuffle=True)

    os.environ['LOKY_MAX_CPU_COUNT'] = '4'
    np.random.seed(7)

    # Loop through each fold
    for train_index, test_index in kfold.split(X_stand):
        # Select the training data
        x_train = X_stand[train_index, :]
        y_train = y[train_index]

        # Train models
        lr_model.fit(x_train, y_train)
        knn_model.fit(x_train, y_train)
        rf_model.fit(x_train, y_train)

        # Make predictions
        lr_pred_fold = lr_model.predict([values])
        knn_pred_fold = knn_model.predict([values])
        rf_pred_fold = rf_model.predict([values])

        # Store predictions
        lr_predictions.append(lr_pred_fold)
        knn_predictions.append(knn_pred_fold)
        rf_predictions.append(rf_pred_fold)

    # Calculate mean predictions
    lr_mean = np.mean(lr_predictions)
    knn_mean = np.mean(knn_predictions)
    rf_mean = np.mean(rf_predictions)

    # Return mean of all models' predictions
    return np.mean([lr_mean, knn_mean, rf_mean])