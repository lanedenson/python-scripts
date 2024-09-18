import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('data.csv')

# Convert dates to numerical values
data['date'] = pd.to_datetime(data['date'])
data['days'] = (data['date'] - data['date'].min()).dt.days

# Prepare the data for each score category
X = data['days'].values.reshape(-1, 1)

# Function to perform linear regression and plot results
def perform_regression(y, y_label):
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    plt.scatter(X, y, color='blue')
    plt.plot(X, y_pred, color='red')
    plt.xlabel('Days')
    plt.ylabel(y_label)
    plt.title(f'{y_label} Over Time')
    plt.show()
    
    print(f"{y_label} - Intercept: {model.intercept_}, Coefficient: {model.coef_[0]}")

# Perform regression for each score category
perform_regression(data['performance_score'], 'Performance Score')
perform_regression(data['accessibility_score'], 'Accessibility Score')
perform_regression(data['best_practices_score'], 'Best Practices Score')
perform_regression(data['seo_score'], 'SEO Score')
