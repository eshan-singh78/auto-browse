import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from datetime import datetime

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def create_logger():
    log_folder = 'log_folder'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    log_filename = f"{log_folder}/browser_automation_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO)

def setup_logger():
    user_input = input("Do you want to create a new logger for this session? (yes/no): ").lower().strip()
    if user_input == 'yes':
        create_logger()
    else:
        log_folder = 'log_folder'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        logging.basicConfig(filename=f'{log_folder}/browser_automation.log', level=logging.INFO)

setup_logger()

def search(query):
    driver.get("https://www.google.com")
    time.sleep(2)
    search_box = driver.find_element("name", "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

def close_overlay():
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, "div.dodTBe")
        close_button.click()
        time.sleep(1)
    except Exception as e:
        print("No overlay to close:", e)

def open_url_by_position(position):
    links = driver.find_elements(By.CSS_SELECTOR, "a")
    valid_links = [link for link in links if link.get_attribute('href')]

    if position <= len(valid_links):
        close_overlay()
        link = valid_links[position - 1]
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(link))
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        
        try:
            link.click()
        except:
            driver.execute_script("arguments[0].click();", link)
        
        time.sleep(2)
    else:
        print("Invalid position! No link found at that position.")

def log_interactive_elements():
    links = driver.find_elements(By.CSS_SELECTOR, "a")
    valid_links = [link for link in links if link.get_attribute('href')]

    logging.info(f"Interactive links on {driver.current_url}:")
    for index, link in enumerate(valid_links, start=1):
        logging.info(f"Position {index}: {link.get_attribute('href')}")

def show_help():
    help_text = """
    Available commands:
    - search <query>     : Perform a Google search with the specified query.
    - open <position>     : Open the link at the given position in the search results.
    - link log           : Log all interactive links on the current page.
    - help               : Show this help message.
    - exit               : Exit the program.
    """
    print(help_text)

def handle_command(command):
    command = command.lower().strip()

    if "search" in command:
        match = re.search(r"search (.+)", command)
        if match:
            search_query = match.group(1)
            search(search_query)
        else:
            print("Please provide a search query after 'search'.")

    elif "open" in command:
        match = re.search(r"open (\d+)", command)
        if match:
            position = int(match.group(1))
            open_url_by_position(position)
        else:
            print("Please provide a valid position after 'open', e.g., 'open 1'.")

    elif "link log" in command:
        log_interactive_elements()

    elif "help" in command:
        show_help()

    else:
        print("Unknown command!")

while True:
    command = input("Enter command (type 'help' to see menu and 'exit' to quit): ")
    if command.lower() == 'exit':
        break
    handle_command(command)

driver.quit()
