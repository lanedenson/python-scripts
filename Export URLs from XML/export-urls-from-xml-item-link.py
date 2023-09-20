import xml.etree.ElementTree as ET
import csv

# Specify the path to the XML input file and the CSV output file
xml_input_file = 'Export URLs from XML\Blogs and Devotionals.xml'
csv_output_file = 'outputbd.csv'


# Parse the XML content from the input file
try:
    with open(xml_input_file, 'r', encoding='utf-8') as xml_file:
        xml_content = xml_file.read()
except FileNotFoundError:
    print(f"Error: File '{xml_input_file}' not found.")
    exit(1)

# Parse the XML content
root = ET.fromstring(xml_content)

# Find and extract the <link> elements within <item> elements
item_links = [item.findtext('link') for item in root.findall('.//item')]

# Sort the links alphabetically
item_links.sort()

# Write the links to a CSV file
try:
    with open(csv_output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Link'])  # Write header row
        for link in item_links:
            csv_writer.writerow([link])
    print(f"Item links extracted, sorted alphabetically, and saved to '{csv_output_file}'.")
except IOError as e:
    print(f"Error: {e}")
