'''
Parse Squarespace/WordPress XML export file
Generate a .txt with all <link> elements sorted alphabetically
'''

import argparse
from bs4 import BeautifulSoup

# Create an argument parser
parser = argparse.ArgumentParser(description='Extract and sort specific <link> elements from an XML file')
parser.add_argument('xml_file', type=str, help='Path to the XML file')

# Parse the command-line arguments
args = parser.parse_args()

# Read the XML file
with open(args.xml_file, 'r', encoding='utf-8') as file:
    xml_content = file.read()

# Parse the XML using BeautifulSoup
soup = BeautifulSoup(xml_content, 'xml')

# Find all the <link> tags
link_tags = soup.find_all('link')

# Extract and sort the href attribute of each <link> element alphabetically
sorted_links = sorted([link.get_text(strip=True) for link in link_tags])

# Print the sorted links
for href in sorted_links:
    print(href)

# Create a text file to store the sorted links
with open('sorted_links.txt', 'w') as file:
    # Write each sorted link to the file
    for href in sorted_links:
        file.write(href + '\n')

print('Links have been exported and sorted alphabetically to sorted_links.txt')
