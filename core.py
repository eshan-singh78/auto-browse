import time
import re
import logging
from control.browser_control import search, open_url_by_position, log_interactive_elements
from control.session_control import create_logger, setup_logger, show_help
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

setup_logger()

def handle_command(command, driver, logging):
    command = command.lower().strip()

    if "search" in command:
        match = re.search(r"search (.+)", command)
        if match:
            search_query = match.group(1)
            search(search_query, driver)
        else:
            print("Please provide a search query after 'search'.")

    elif "open" in command:
        match = re.search(r"open (\d+)", command)
        if match:
            position = int(match.group(1))
            open_url_by_position(position, driver)
        else:
            print("Please provide a valid position after 'open', e.g., 'open 1'.")

    elif "link log" in command:
        log_interactive_elements(driver, logging)

    elif "help" in command:
        show_help()

    else:
        print("Unknown command!")

while True:
    command = input("Enter command (type 'help' to see menu and 'exit' to quit): ")
    if command.lower() == 'exit':
        break
    handle_command(command, driver, logging)
    
driver.quit()
