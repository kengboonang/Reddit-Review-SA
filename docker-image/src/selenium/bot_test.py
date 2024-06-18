from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.reddit.com/r/googleReviews/")
assert "google reviews" in driver.title
driver.implicitly_wait(20)  # Waits for 10 seconds

# Scroll down to load more content
for _ in range(10):  # Adjust the range for more scrolling
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)  # Wait for content to load


elem = driver.find_elements(By.CSS_SELECTOR, "div[data-post-click-location='text-body'] p")
# for element in elem:
#     print(element.text)
print(elem)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()