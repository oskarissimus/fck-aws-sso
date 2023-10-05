import sys
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def authorize_sso(url, code):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    try:
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "verification_code"))
        )
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cli_verification_btn"))
        )
        input_element.send_keys(code)
        submit_button.click()

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cli_login_button"))
        )
        login_button.click()

        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()


def extract_url_and_code(text):
    url_pattern = r"https://[a-zA-Z0-9./_-]+"
    code_pattern = r"\b[A-Z0-9]{4}-[A-Z0-9]{4}\b"

    url = re.search(url_pattern, text).group()
    code = re.search(code_pattern, text).group()

    return url, code


def main():
    # Read from stdin
    input_text = sys.stdin.read()

    # Extract URL and code
    extracted_url, extracted_code = extract_url_and_code(input_text)

    # Interact with the webpage using Selenium
    authorize_sso(extracted_url, extracted_code)


if __name__ == "__main__":
    main()
