# Calculate the average Lighthouse score improvements over time for
# Performance Score, Accessibility Score, Best Practices Score, and SEO Score

import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression

# Directory containing the CSV files
directory = r'.\csv'

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

# Drop rows with any missing values
combined_data = combined_data.dropna()

# Prepare the data for each score category
X = combined_data['days'].values.reshape(-1, 1)

# Function to perform linear regression and calculate percentage improvement
def calculate_percentage_improvement(y, y_label):
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    initial_value = y_pred[0]
    final_value = y_pred[-1]
    percentage_improvement = ((final_value - initial_value) / initial_value) * 100

    return percentage_improvement

# Calculate percentage improvement for each score category
for score, label in zip(
    [combined_data['performance_score'], combined_data['accessibility_score'], 
     combined_data['best_practices_score'], combined_data['seo_score']],
    ['Performance Score', 'Accessibility Score', 'Best Practices Score', 'SEO Score']
):
    improvement = calculate_percentage_improvement(score, label)
    print(f"{label} - Percentage Improvement: {improvement:.2f}%")

# Calculate the highest average score for each category
average_scores = {
    'Performance Score': combined_data['performance_score'].mean(),
    'Accessibility Score': combined_data['accessibility_score'].mean(),
    'Best Practices Score': combined_data['best_practices_score'].mean(),
    'SEO Score': combined_data['seo_score'].mean()
}

# Print the highest average scores for each column
for label, avg_score in average_scores.items():
    print(f"{label} - Highest Average Score: {avg_score:.2f}")