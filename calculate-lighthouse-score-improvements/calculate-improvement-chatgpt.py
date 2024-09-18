import pandas as pd

# Load data from CSV file
file_path = 'data.csv'  # Update with your CSV file path
df = pd.read_csv(file_path)

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Ensure all required columns are present
required_columns = ['date', 'performance_score', 'accessibility_score', 'best_practices_score', 'seo_score']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

# Calculate daily differences
df['performance_diff'] = df['performance_score'].diff()
df['accessibility_diff'] = df['accessibility_score'].diff()
df['best_practices_diff'] = df['best_practices_score'].diff()
df['seo_diff'] = df['seo_score'].diff()

# Average improvements over time
average_improvements = df[['performance_diff', 'accessibility_diff', 'best_practices_diff', 'seo_diff']].mean()

print("Average improvements over time:")
print(average_improvements)
