import json

# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL to scrape
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

time.sleep(2)

# Results
result_items = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
print(f"Found {len(result_items)} results")

results = []

for item in result_items:
    # Extract title
    title_elem = item.find_element(By.CSS_SELECTOR, "span.title-content")
    title = title_elem.text if title_elem else "No title"

    # Extract authors (may be multiple)
    author_elems = item.find_elements(By.CSS_SELECTOR, "a.author-link")
    authors = [a.text for a in author_elems if a.text]
    author_str = "; ".join(authors) if authors else "Unknown"

    # Extract format and year
    format_elem = item.find_element(By.CSS_SELECTOR, "span.display-info-primary")
    format_year = format_elem.text if format_elem else "No format info"

    results.append({
        "Title": title,
        "Author": author_str,
        "Format-Year": format_year
    })

# Task 4: Write JSON file
with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Saved to get_books.json")

# Close the driver
driver.quit()

# Create DataFrame and print
df = pd.DataFrame(results)
print("\nDataFrame:")
print(df)

# Save to CSV
df.to_csv("get_books.csv", index=False)
print("\nSaved to get_books.csv")