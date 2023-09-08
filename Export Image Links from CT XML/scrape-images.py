'''
Parse Squarespace/WordPress XML export file
Generate a .txt file with all URLs that contain PNG and JPG references
'''

import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Function to extract image URLs from CDATA
def extract_image_urls(xml_file):
    image_urls = []
    
    # Define XML namespaces
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
    }
    
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Find all <content:encoded> elements
    content_encoded_elements = root.findall('.//content:encoded', namespaces=namespaces)
    
    # Loop through <content:encoded> elements to extract image URLs
    for content_encoded in content_encoded_elements:
        cdata = content_encoded.text
        
        # Parse the CDATA content with BeautifulSoup
        soup = BeautifulSoup(cdata, 'html.parser')
        
        # Find all <img> tags
        img_tags = soup.find_all('img')
        
        # Extract the 'src' attribute from each <img> tag
        for img_tag in img_tags:
            src = img_tag.get('src')
            
            # Check if the URL has JPG or PNG extensions and add to the list
            if src.lower().endswith('.jpg') or src.lower().endswith('.png'):
                image_urls.append(src)
    
    return image_urls

# Function to export the list of URLs to a text file
def export_to_txt(image_urls, output_file):
    with open(output_file, 'w') as txt_file:
        for url in image_urls:
            txt_file.write(url + '\n')

# Usage example
if __name__ == "__main__":
    xml_file = 'blogs-and-devotionals.xml'  # Replace with your XML file path
    output_txt_file = 'output_image_urls.txt'  # Replace with the desired output file name
    
    image_urls = extract_image_urls(xml_file)
    
    # Export the list of image URLs to a text file
    export_to_txt(image_urls, output_txt_file)
    
    print(f"Image URLs exported to '{output_txt_file}'.")
