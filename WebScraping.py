#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


url = "https://www.gamespot.com/reviews/the-last-of-us-part-i-ps5-and-pc-review-desolation-row/1900-6417949/"


response = requests.get(url)


if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    paragraphs = soup.find_all("p")
    
   
    for paragraph in paragraphs:
        print(paragraph.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)





import requests
from bs4 import BeautifulSoup
from summarizer import Summarizer
import warnings

warnings.filterwarnings("ignore")


url = input("Enter the url to scrape")


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    paragraphs = soup.find_all("p")
    
    
    text = "\n".join(paragraph.get_text() for paragraph in paragraphs)
    
   
    summarizer = Summarizer()
    
    
    summary = summarizer(text, ratio=0.2)  # You can adjust the 'ratio' for the desired summary length
    
    
    print(summary)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)







