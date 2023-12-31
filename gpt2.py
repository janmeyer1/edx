from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from twilio.rest import Client

def run_script():
    url = "https://www-genesis.destatis.de/genesis//online?operation=table&code=61111-0002&bypass=true&levelindex=0&levelid=1700395649160#abreadcrumb"

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode, without GUI
    chrome_options.add_argument("--disable-gpu")  # Disable GPU to avoid some issues

    # Start the WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn-flex-grid' and @name='werteabruf']")))

        # Find the "Werteabruf" button and click it
        werteabruf_button = driver.find_element(By.XPATH, "//button[@class='btn-flex-grid' and @name='werteabruf']")
        werteabruf_button.click()

        # Wait for the results to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ET")))

        # Extract and print the table data with row and column headers
        table = driver.find_element(By.ID, "ET")
        rows = table.find_elements(By.TAG_NAME, "tr")

        result_data = ""

        for i, row in enumerate(rows):
            cells = row.find_elements(By.TAG_NAME, "td")
            headers = row.find_elements(By.TAG_NAME, "th")

            # Print column headers
            if i == 0:
                for header in headers:
                    result_data += f"{header.text}\t"
                result_data += "\n"

            # Print row header
            if headers:
                result_data += f"{headers[-1].text}\t"

            # Print cell data
            for cell in cells:
                result_data += f"{cell.text}\t"
            result_data += "\n"

    finally:
        # Close the browser window
        driver.quit()

    return result_data

def send_whatsapp_message(message):
    # Twilio credentials
    account_sid = 'ACfe445b759c0bb088bc79e704f6886426'
    auth_token = 'd377bc87ced004775858d0e0e5ce7279'
    twilio_phone_number = '+14155238886'
    your_phone_number = '+4915174278492'

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send WhatsApp message
    message = client.messages.create(
        from_='whatsapp:' + twilio_phone_number,
        body=message,
        to='whatsapp:' + your_phone_number
    )

# Schedule the script to run every Sunday at noon
schedule.every().sunday.at("14:39").do(lambda: send_whatsapp_message(run_script()))

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
