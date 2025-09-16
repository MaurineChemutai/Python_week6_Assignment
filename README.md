# Ubuntu Image Fetcher 🖼️✨

**Ubuntu-Inspired Image Fetcher Assignment**  
> *"I am because we are."* – Ubuntu Philosophy  

This is a Python-based tool that embraces the spirit of **Ubuntu** — community, respect, sharing, and practicality.  
It allows users to fetch and organize images from the internet in a mindful and respectful way.  

---

## 🌍 Project Overview
The **Ubuntu Image Fetcher** is a command-line tool that:
- Prompts the user to enter a URL containing an image.  
- Creates a directory called **`Fetched_Images`** if it does not exist.  
- Downloads the image and saves it into the directory.  
- Handles errors gracefully, respecting that not all connections succeed.  
- Names the image appropriately based on the URL or generates a default filename.  

---

## ✨ Features
- ✅ Uses the `requests` library to fetch images.  
- ✅ Graceful error handling for network or HTTP issues.  
- ✅ Automatically creates the `Fetched_Images` folder.  
- ✅ Extracts filenames from URLs or generates a fallback name.  
- ✅ Saves images in **binary mode** for integrity.  
