from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tempfile import mkdtemp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time,json
import unittest
def lambda_handler1(event=None, context=None):
   print("test1")
def lambda_handler(event=None, context=None):
    

    chrome_options = Options()

    chrome_options.browser_version = "130"
    chrome_options.platform_name = "Windows 10"
    lt_options = {};
    lt_options["username"] = "hieuphp";
    lt_options["accessKey"] = "W5TppfW5ggLomrpcHzPJmcyGsjghtEGMTqZZadUdS6XJjgxJ86";
    lt_options["smartUI.project"] = "fff";
    lt_options["resolution"] = "1024x768";
    lt_options["recordVideo"] = "true";
    lt_options["browserName"] = "Chrome";
    lt_options["w3c"] = True;
    lt_options["selenium_version"] = "4.0.0";
    lt_options["plugin"] = "python-python";
    chrome_options.set_capability('LT:Options', lt_options);

    # Desired capabilities can be set directly in the options if needed

        # Initialize Remote WebDriver with command_executor and desired capabilities
    driver = webdriver.Remote(command_executor="http://hub.lambdatest.com:80/wd/hub",options=chrome_options)

    driver.get("https://id.chotot.com/?continue=https://chat.chotot.com/chat")
    time.sleep(1)
    try:
        # Tìm và click vào nút "Login với Google"
        submit_button = driver.find_elements(By.CSS_SELECTOR, 'button.mocked-styled-18.b10u9umr')[1]
        actions = ActionChains(driver)
        actions.click_and_hold(submit_button).pause(2).release().perform()
        # Kiểm tra nếu có ít nhất 2 nút  
    except Exception as e:
        print("click xong")

    
  
    driver.quit()
    return {
        "statusCode": 200,
        "body": f"{title}"
    }
lambda_handler(1,2)
