import logging
import os
from datetime import datetime

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
