# Auto-Browse 

This project automates web browsing actions using Selenium WebDriver. It allows users to perform searches, open links from search results, log interactive elements on the page, and more. The project is organized into separate modules for browser control and session control.

## Features

- **Search**: Perform a Google search with a specific query.
- **Open Link by Position**: Open a link from the search results based on its position.
- **Link Logging**: Log all interactive links on the current page.
- **Session Logging**: Create and manage log files for browser interactions.
- **Help**: Display a help message with available commands.

## Project Structure

```
auto-browse/
├── control/
│   ├── browser_control.py  # Functions for browser-related actions (search, open link, etc.)
│   └── session_control.py  # Functions for session management (logger, help)
├── core.py                 # Main script to handle user commands and interact with browser
└── requirements.txt        # Python dependencies for the project
```

### Control Folder

The `control` folder contains two Python files:

1. **`browser_control.py`**: Handles browser-related actions like performing a search, opening links by position, and logging interactive elements on the page.
2. **`session_control.py`**: Manages session tasks such as setting up the logger and displaying the help message.

### Main Script

- **`core.py`**: This is the main script that runs the program. It accepts user commands, interacts with the browser, and logs actions.

## Requirements

- Python 3.x
- Selenium
- webdriver-manager

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/auto-browse.git
   cd auto-browse
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv autobrowseenv
   source autobrowseenv/bin/activate  # On Windows, use autobrowseenv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:

   ```bash
   python core.py
   ```

2. The program will prompt you to decide if you want to create a new logger for the session.

3. Enter commands as prompted:

   - `search <query>`: Perform a Google search with the specified query.
   - `open <position>`: Open the link at the given position from the search results.
   - `link log`: Log all interactive links on the current page.
   - `help`: Show available commands.
   - `exit`: Exit the program.

Example:

```
Enter command (type 'help' to see menu and 'exit' to quit): search python selenium
Enter command (type 'help' to see menu and 'exit' to quit): open 1
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Create a pull request.

