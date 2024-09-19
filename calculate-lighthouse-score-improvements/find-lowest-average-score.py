# This script finds the file with the lowest average score for each metric

from pathlib import Path
import pandas as pd

# Directory containing the CSV files
directory = Path(__file__).parent / 'csv'

# Define labels
PERF = 'Performance Score'
ACC = 'Accessibility Score'
BP = 'Best Practices'
SEO = 'SEO Score'
METRICS = [PERF, ACC, BP, SEO]

# Initialize dictionaries to store the lowest and highest average scores and corresponding files
lowest_avg_files = {metric: None for metric in METRICS}
lowest_avg_values = {metric: float('inf') for metric in METRICS}
highest_avg_files = {metric: None for metric in METRICS}
highest_avg_values = {metric: float('-inf') for metric in METRICS}

# Function to calculate the average score for each metric
def calculate_average_scores(data):
    return {
        PERF: data['performance_score'].mean(),
        ACC: data['accessibility_score'].mean(),
        BP: data['best_practices_score'].mean(),
        SEO: data['seo_score'].mean()
    }

# Loop through all CSV files in the directory and calculate average scores
for file_path in directory.glob('*.csv'):
    try:
        data = pd.read_csv(file_path, usecols=['performance_score', 'accessibility_score', 'best_practices_score', 'seo_score']).dropna()
        avg_scores = calculate_average_scores(data)

        # Update the lowest and highest average scores and corresponding files
        for metric, score in avg_scores.items():
            if score < lowest_avg_values[metric]:
                lowest_avg_values[metric] = score
                lowest_avg_files[metric] = file_path.name
            if score > highest_avg_values[metric]:
                highest_avg_values[metric] = score
                highest_avg_files[metric] = file_path.name
    except Exception as e:
        print(f"Error processing file {file_path.name}: {e}")

# Print the results
for metric in METRICS:
    print(f"\nLowest Average {metric}: {lowest_avg_values[metric]:.2f}\nFile: {lowest_avg_files[metric]}")
    print(f"\nHighest Average {metric}: {highest_avg_values[metric]:.2f}\nFile: {highest_avg_files[metric]}\n")
