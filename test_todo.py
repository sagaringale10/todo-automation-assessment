from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Provide the path to your ChromeDriver
service = Service(r'C:\Users\sagar\Desktop\Sagar congnizant\chromedriver-win64\chromedriver-win64')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

try:
    # Open the ToDoMVC application
    driver.get("https://todomvc.com/examples/react/dist/")
    print("Successfully opened ToDoMVC app.")

    # Verify the page loads by checking the presence of the input box
    input_box = driver.find_element(By.CLASS_NAME, "new-todo")
    if input_box:
        print("Test Passed: ToDo input box is present.")
    else:
        print("Test Failed: ToDo input box is missing.")
finally:
    # Close the browser
    driver.quit()
