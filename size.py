import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

def predict_property_size(data):
    # Extracting features and target for training data
    X_train = data.dropna(subset=['Size']).drop('Size', axis=1).to_numpy()
    y_train = data.dropna(subset=['Size'])['Size'].to_numpy()
    y_train = y_train[:, None]
    y_train = y_train.ravel()

    # Extracting features for prediction data
    X_pred = data[data['Size'].isna()].drop('Size', axis=1).to_numpy() 

    # Set random seed for reproducibility
    np.random.seed(7)

    # Models initialization
    models = {
        'Linear Regression': LinearRegression(),
        'KNN Regression': KNeighborsRegressor(),
        'Random Forest Regression': RandomForestRegressor()
    }

    # Initialize an empty DataFrame to store predicted values for each model
    predictions = pd.DataFrame(columns=list(models.keys()))

    # Iterate through each model for training, prediction, and plotting
    for model_name, model in models.items():
        # Fit the model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_pred)

        # Store predicted values in the predictions DataFrame
        y_pred = pd.DataFrame(y_pred, columns=['Size'])
        predictions[model_name] = y_pred

        # Combine predictions with features
        data_pred = pd.concat([pd.DataFrame(X_pred, columns=data.columns[:-1]), y_pred], axis=1)
        # Add 'Source' column to indicate predicted values
        data_pred['Source'] = 'Predicted'

        # Combine predicted and actual data for visualization
        data_combined = pd.concat([data.dropna(subset=['Size']).copy(), data_pred])
        data_combined.loc[:, 'Source'] = data_combined['Source'].fillna('Given')

        # Plot scatterplot for model predictions
        plt.figure()
        sns.scatterplot(data=data_combined, x='Price', y='Size', hue='Source')
        plt.title(f'{model_name} Predictions')

    plt.show()

    # Compute the mean of all different types of predictions
    predictions['Size'] = predictions.mean(axis=1)

    # Save the mean predicted value in a DataFrame
    size = pd.DataFrame(predictions['Size'])

    # Combine predictions with features and add a column 'Source' to indicate the predicted values
    size_pred = pd.concat([pd.DataFrame(X_pred, columns=data.columns[:-1]), size], axis=1)
    size_pred['Source'] = 'Predicted'

    # Combine predicted data with actual data
    data_full = pd.concat([data.dropna(subset=['Size']).copy(), size_pred])
    data_full.loc[:, 'Source'] = data_full['Source'].fillna('Given')

    # Plot the scatter plot of price against size and use the 'Source' variable as the color indicator
    print("Scatter plot of 'correct' values:")
    sns.scatterplot(data=data_full, x='Size', y='Price', hue='Source')
    plt.show()

    return data_full