from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search(query, driver):
    driver.get("https://www.google.com")
    time.sleep(2)
    search_box = driver.find_element("name", "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

def open_url_by_position(position, driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a")
    valid_links = [link for link in links if link.get_attribute('href')]

    if position <= len(valid_links):
        link = valid_links[position - 1]
        link.click()
        time.sleep(2)
    else:
        print("Invalid position! No link found at that position.")

def log_interactive_elements(driver, logging):
    links = driver.find_elements(By.CSS_SELECTOR, "a")
    valid_links = [link for link in links if link.get_attribute('href')]

    logging.info(f"Interactive links on {driver.current_url}:")
    for index, link in enumerate(valid_links, start=1):
        logging.info(f"Position {index}: {link.get_attribute('href')}")
