#required packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to the chromedriver exe file
chromedriver_path = '..\..\.cache\selenium\chromedriver\win32\109.0.5414.74'

# Create a new instance of Chrome driver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Go to Amazon India
driver.get('https://www.amazon.in')

# Fill the search form and click submit button
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('Wrist Watches')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

# Select "Analogue"
display_select = driver.find_element(By.LINK_TEXT, 'Analogue')
display_select.click()

# Select "Leather"
material_select = driver.find_element(By.LINK_TEXT, 'Leather')
material_select.click()

# Select "Titan"
brand_select = driver.find_element(By.LINK_TEXT, 'Titan')
brand_select.click()

# delay for element to be selectable
time.sleep(5)

# Select "25% Off or more"
discount_select = driver.find_element(By.LINK_TEXT, '25% Off or more')
discount_select.click()

# delay to wait for element
time.sleep(5)

# Get the fifth element from the search results
search_results = driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
if len(search_results) >= 5:
    fifth_element = search_results[4]
    print(fifth_element.text)
else:
    print("Not enough search results to retrieve the fifth element.")

# Close the browser window
driver.quit()
