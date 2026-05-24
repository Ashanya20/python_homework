# Task 6: Scrape OWASP Top 10 vulnerabilities

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to main page
driver.get("https://owasp.org/www-project-top-ten/")

# Click the link to the 2025 list
driver.find_element(By.LINK_TEXT, "OWASP Top Ten 2025").click()
time.sleep(2)  # wait for page to load

# Extract the 10 items using XPath
results = []
for i in range(1, 11):
    xpath = f"/html/body/div[3]/main/div/div[3]/article/ol/li[{i}]/a"
    elem = driver.find_element(By.XPATH, xpath)
    title = elem.text
    link = elem.get_attribute("href")
    results.append({"Title": title, "Link": link})

driver.quit()

# Print the list
print(results)

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)