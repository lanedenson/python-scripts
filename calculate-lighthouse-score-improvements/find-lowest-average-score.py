import pandas as pd
import os
from sklearn.linear_model import LinearRegression

# Directory containing the CSV files
directory = os.path.join(os.path.dirname(__file__), 'csv')

# Initialize a dictionary to store the average scores for each file
file_scores = {}

# Function to calculate the average score for each metric
def calculate_average_scores(data):
    return {
        'Performance Score': data['performance_score'].mean(),
        'Accessibility Score': data['accessibility_score'].mean(),
        'Best Practices Score': data['best_practices_score'].mean(),
        'SEO Score': data['seo_score'].mean()
    }

# Loop through all CSV files in the directory and calculate average scores
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        data = pd.read_csv(file_path)

        # Keep only the relevant columns
        data = data[['date', 'performance_score', 'accessibility_score', 'best_practices_score', 'seo_score']]

        # Drop rows with any missing values
        data = data.dropna()

        # Calculate average scores for the current file and store them
        avg_scores = calculate_average_scores(data)
        file_scores[filename] = avg_scores

# Identify the file with the lowest average score for each metric
lowest_avg_files = {metric: None for metric in ['Performance Score', 'Accessibility Score', 'Best Practices Score', 'SEO Score']}
lowest_avg_values = {metric: float('inf') for metric in ['Performance Score', 'Accessibility Score', 'Best Practices Score', 'SEO Score']}

for filename, scores in file_scores.items():
    for metric, score in scores.items():
        if score < lowest_avg_values[metric]:
            lowest_avg_values[metric] = score
            lowest_avg_files[metric] = filename

# Print the results
for metric, filename in lowest_avg_files.items():
    print(f"Lowest Average {metric}: {lowest_avg_values[metric]:.2f} found in file: {filename}")
