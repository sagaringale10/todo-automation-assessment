# To-Do Automation Assessment

## Overview
This repository contains automated tests for the To-Do MVC application provided as part of Cognizant's Automation Technical Challenge. The goal of the tests is to verify key functionalities of the application, ensuring users can manage their to-dos effectively.

## Tools and Technologies Used
- **Programming Language:** Python
- **Automation Tool:** Selenium
- **Browser Driver:** ChromeDriver

## Acceptance Criteria
The following features were tested based on the provided user story:

1. **Adding a To-Do**:
   - The user can add a task via the input box.
   - The task is displayed in the list immediately after adding.

2. **Marking a To-Do as Completed**:
   - The user can mark tasks as completed using a checkbox.
   - Completed tasks show a strikethrough effect.

3. **Editing a To-Do**:
   - Double-clicking a task enables editing mode.
   - Tasks can be updated by pressing Enter or canceled by pressing Esc.

4. **Deleting a To-Do**:
   - Hovering over a task shows a delete button.
   - Clicking the delete button removes the task.

5. **Filtering To-Dos**:
   - The user can filter tasks (All, Active, Completed).
   - Filters display tasks correctly based on their status.

## Prerequisites
Before running the tests, ensure the following are installed:
- Python (3.7 or higher)
- Selenium (`pip install selenium`)
- ChromeDriver (compatible with your Chrome browser version)

## Project Structure
```
.
|-- test_add_todo.py        # Test for adding a to-do
|-- test_complete_todo.py   # Test for marking a to-do as completed
|-- test_edit_todo.py       # Test for editing a to-do
|-- test_delete_todo.py     # Test for deleting a to-do
|-- test_filter_todo.py     # Test for filtering to-dos
|-- requirements.txt        # Dependencies for the project
```

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download ChromeDriver:**
   - Download the ChromeDriver matching your Chrome browser version.
   - Place the `chromedriver.exe` file in the root directory.

## Running the Tests
To run a specific test, use the following command:
```bash
python test_add_todo.py
```
Replace `test_add_todo.py` with the desired test file.

## Implementation Strategy
The automation tests were designed to:
- Identify key elements of the application using unique identifiers (e.g., class names or IDs).
- Automate user actions such as adding, editing, or deleting tasks.
- Validate the expected outcomes using assertions.

