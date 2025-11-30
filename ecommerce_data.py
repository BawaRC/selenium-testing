from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the site
driver.get("https://www.saucedemo.com/") # demo ecommerce website for automated data extraction testing

# Wait for page to load
time.sleep(2)

# Login with demo credentials
driver.find_element(By.ID, "user-name").send_keys("") # your demo login username 
driver.find_element(By.ID, "password").send_keys("") #your demo login password
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Now we're on the products page
# Get all product elements
product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

# Display data in terminal
print("\n🛒 Available Products:\n")
for name, price in zip(product_names, product_prices):
    print(f"{name.text} - {price.text}")

# (Optional) Click a product to see details
product_names[0].click()
time.sleep(2)
print("\n➡️ Viewing product details page:", driver.current_url)

# Quit browser
driver.quit()


