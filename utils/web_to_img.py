from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os

def capture_fullpage_screenshot(url, folder):
    """
    Captures a full-page screenshot of a given URL and saves it to a specified folder.

    :param url: The URL of the webpage to capture.
    :param folder: The folder where the screenshot will be saved.
    """
    # Sanitize the URL to create a valid filename
    filename = url.replace("http://", "").replace("https://", "").replace("/", "_")
    filename = (filename[:200] + '..') if len(filename) > 200 else filename  # Truncate if too long
    output_file = os.path.join(folder, filename + ".jpg")  # Save as .png

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(ChromeDriverManager().install())

    # Choose Chrome Browser
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Open URL
    driver.get(url)

    # Give time for the page to load
    time.sleep(10)

    # Set the width and height of the browser to the full page
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)

    # Take screenshot
    driver.save_screenshot(output_file)
    driver.quit()

# Example usage
#capture_fullpage_screenshot('https://jobs.franciscanhealth.org/us/en/job/R-093330/Medical-Assistant-or-LPN-Physician-Practice-Sign-On-Bonus-Available', '/Users/zhilinwang/PycharmProjects/Anton_TalnF/data/CV')
