# Calculate the average Lighthouse score improvements over time for
# Performance Score, Accessibility Score, Best Practices Score, and
# SEO Score from CSV data.

import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression

# Directory containing the CSV files
directory = os.path.join(os.path.dirname(__file__), 'umc-csv')

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through all CSV files in the directory and concatenate them
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        data = pd.read_csv(file_path)

        # Keep only the relevant columns
        data = data[['date', 'performance_score', 'accessibility_score', 'best_practices_score', 'seo_score']]

        combined_data = pd.concat([combined_data, data], ignore_index=True)

# Convert dates to numerical values
combined_data['date'] = pd.to_datetime(combined_data['date'])
combined_data['days'] = (combined_data['date'] - combined_data['date'].min()).dt.days

# Filter data for dates after September 11
start_date = pd.to_datetime('2024-09-11')  # Adjust the year as necessary
filtered_data = combined_data[combined_data['date'] >= start_date]

# Drop rows with any missing values, where scores are 0, or where scores are above 100
filtered_data = filtered_data.dropna()
filtered_data = filtered_data[(filtered_data[['performance_score', 'accessibility_score', 
                                               'best_practices_score', 'seo_score']] != 0).all(axis=1)]
filtered_data = filtered_data[(filtered_data[['performance_score', 'accessibility_score', 
                                               'best_practices_score', 'seo_score']] <= 100).all(axis=1)]

# Prepare the data for each score category
X_filtered = filtered_data['days'].values.reshape(-1, 1)

# Function to perform linear regression and calculate percentage improvement
def calculate_percentage_improvement(y):
    model = LinearRegression()
    model.fit(X_filtered, y)
    y_pred = model.predict(X_filtered)

    initial_value = y_pred[0]
    final_value = y_pred[-1]
    percentage_improvement = ((final_value - initial_value) / initial_value) * 100

    return percentage_improvement

# Calculate percentage improvement for each score category since September 11
for score, label in zip(
    [filtered_data['performance_score'], filtered_data['accessibility_score'], 
     filtered_data['best_practices_score'], filtered_data['seo_score']],
    ['Performance Score', 'Accessibility Score', 'Best Practices Score', 'SEO Score']
):
    improvement = calculate_percentage_improvement(score)
    print(f"{label} - Percentage Improvement since September 11: {improvement:.2f}%")

print ()

# Calculate the highest average score for each category
average_scores = {
    'Performance Score': filtered_data['performance_score'].mean(),  # Use filtered_data here
    'Accessibility Score': filtered_data['accessibility_score'].mean(),
    'Best Practices Score': filtered_data['best_practices_score'].mean(),
    'SEO Score': filtered_data['seo_score'].mean()
}

# Print the highest average scores for each column
for label, avg_score in average_scores.items():
    print(f"{label} - Highest Average Score: {avg_score:.2f}")