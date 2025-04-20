#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests beautifulsoup4 pandas


# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lists to store the scraped data
all_quotes = []
all_authors = []
all_tags = []

# Base URL for pagination
base_url = "http://quotes.toscrape.com/page/{}/"

# Loop through the first 10 pages
for page in range(1, 11):
    url = base_url.format(page)
    response = requests.get(url)

    # Check if the page is successfully retrieved
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        continue

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all("div", class_="quote")

    # Extract quotes, authors, and tags from each quote
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        # Append the data to the lists
        all_quotes.append(text)
        all_authors.append(author)
        all_tags.append(", ".join(tags))  # Join multiple tags into a single string

# Create a DataFrame to organize the data
df = pd.DataFrame({
    "Quote": all_quotes,
    "Author": all_authors,
    "Tags": all_tags
})

# Save the data to a CSV file
df.to_csv("quotes_scraper_output.csv", index=False)

print("✅ Scraping completed. Saved as quotes_scraper_output.csv")



# In[2]:


import os
print("Current working directory:", os.getcwd())


# In[ ]:




