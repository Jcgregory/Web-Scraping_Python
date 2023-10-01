# R program to illustrate
# Web Scraping

# Import rvest library
library(rvest)

# Reading the HTML code from the website
webpage = read_html("https://www.reddit.com/r/movies/comments/16wr8ih/who_in_your_opinion_is_the_greatest_current/")

# Using CSS selectors to scrape the heading section
heading = html_node(webpage, '.entry-title')

# Converting the heading data to text
text = html_text(heading)
print(text)

# Using CSS selectors to scrape
# all the paragraph section
# Note that we use html_nodes() here
paragraph = html_nodes(webpage, 'p')

# Converting the heading data to text
pText = html_text(paragraph)

# Print the top 6 data
print(head(pText))
