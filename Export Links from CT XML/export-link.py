import argparse
from bs4 import BeautifulSoup

# Create an argument parser
parser = argparse.ArgumentParser(description='Extract data within <link></link> tags from an XML file')
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

# Create a text file to store the links
with open('links.txt', 'w') as file:
    # Write each link to the file
    for link in link_tags:
        file.write(link.text + '\n')

print('Links have been exported to links.txt')
