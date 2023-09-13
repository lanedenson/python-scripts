'''
Extract filenames from a list of URLs in a txt file
'''

import os

def extract_filenames_from_urls(url_list):
    filenames = []
    
    for url in url_list:
        # Split the URL by the forward slash '/'
        parts = url.split('/')
        
        # Get the last part of the URL (which should be the filename)
        filename = parts[-1]
        
        # Add the filename to the list
        filenames.append(filename)
    
    return filenames

def read_urls_from_file(filename):
    try:
        with open(filename, 'r') as file:
            urls = file.read().splitlines()
        return urls
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Example usage
if __name__ == "__main__":
    input_filename = "urls.txt"  # Replace with the path to your text file

    url_list = read_urls_from_file(input_filename)
    
    if url_list:
        extracted_filenames = extract_filenames_from_urls(url_list)
    
        for i, filename in enumerate(extracted_filenames):
            print(f"URL {i + 1}: {filename}")
