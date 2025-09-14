#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL(s) from user
    urls = input("Please enter image URL(s), separated by commas: ").split(",")
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    
    # Keep track of already downloaded files to avoid duplicates
    downloaded_files = set(os.listdir("Fetched_Images"))
    
    for url in urls:
        url = url.strip()  # remove spaces
        if not url:
            continue  # skip empty input
        
        try:
            # Fetch the image with timeout and error handling
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # raise error for bad status codes
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename:  # if URL doesn't have a filename
                filename = "downloaded_image.jpg"
            
            # Prevent duplicates
            if filename in downloaded_files:
                print(f"⚠ Skipped duplicate: {filename}")
                continue
            
            # Save the image
            filepath = os.path.join("Fetched_Images", filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            downloaded_files.add(filename)  # track saved file
            
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        
        except requests.exceptions.RequestException as e:
            # Respect: handle web-related errors gracefully
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"✗ An error occurred for {url}: {e}")
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

    


# In[ ]:




