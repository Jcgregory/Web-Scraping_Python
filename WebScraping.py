#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.gamespot.com/reviews/the-last-of-us-part-i-ps5-and-pc-review-desolation-row/1900-6417949/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and extract text from specific elements (e.g., <p> tags)
    paragraphs = soup.find_all("p")
    
    # Extract and print text from each paragraph
    for paragraph in paragraphs:
        print(paragraph.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


# In[5]:


import requests
from bs4 import BeautifulSoup
from summarizer import Summarizer
import warnings

warnings.filterwarnings("ignore")

# URL of the website to scrape
url = input("Enter the url to scrape")

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and extract text from specific elements (e.g., <p> tags)
    paragraphs = soup.find_all("p")
    
    # Extract and concatenate text from paragraphs into a single text
    text = "\n".join(paragraph.get_text() for paragraph in paragraphs)
    
    # Create a BERT-based summarizer
    summarizer = Summarizer()
    
    # Generate a summary
    summary = summarizer(text, ratio=0.2)  # You can adjust the 'ratio' for the desired summary length
    
    # Print the summary
    print(summary)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


# In[ ]:




