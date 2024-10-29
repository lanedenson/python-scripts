import requests
import csv

# File names for input and output
input_file = "input_urls.txt"  # Text file with each URL on a new line
output_file = "url_status_check.csv"

# Read URLs from the text file
with open(input_file, "r") as file:
    urls = [line.strip() for line in file if line.strip()]  # Remove any empty lines

# Open CSV file for writing
with open(output_file, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(["URL", "Status"])

    # Check each URL
    for url in urls:
        try:
            response = requests.head(url, timeout=5)  # Using HEAD request for efficiency
            status = "404" if response.status_code == 404 else "OK"
            writer.writerow([url, status])
            print(f"Checked URL: {url}, Status: {status}")  # Display URL and status in terminal
        except requests.RequestException as e:
            writer.writerow([url, "Error"])
            print(f"Checked URL: {url}, Status: Error")  # Display URL and error in terminal

print(f"URL check complete. Results saved to {output_file}.")
