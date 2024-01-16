
## import libray
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import bs4
import pandas as pd

# Set up Chrome WebDriver
driver = webdriver.Chrome(options=Options())
url = 'https://www.bbc.com/news'
driver.get(url)

# Wait for the page to load (adjust sleep duration if needed)
sleep(2)

# Extract data using BeautifulSoup
soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
titles = []
categories = []

# Scraping the first 100 articles
for article in soup.find_all("div", class_="gs-c-promo-body"):
    if len(titles) >= 100:
        break
    title_element = article.find("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")
    category_element = article.find("a", class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state")
    if title_element and category_element:
        titles.append(title_element.text.strip())
        categories.append(category_element.text.strip())

# Close the WebDriver
driver.quit()

# Create DataFrame and export to CSVand
df = pd.DataFrame({"Title": titles, "Category": categories})
df.to_csv("bbc_news_scraping.csv", index=False)
