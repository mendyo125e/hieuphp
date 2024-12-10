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

s3_client = boto3.client('s3')
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

    body_element = driver.find_element("tag name", "body").text  # Tìm thẻ <body>
    print("Nội dung văn bản của <body>:", body_element)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    title = driver.title
    
    timeout = 1
    all_windows = driver.window_handles

# Chuyển đến cửa sổ mới (là cửa sổ thứ hai trong danh sách)
    driver.switch_to.window(all_windows[1])
    end_time = time.time() + timeout

    time.sleep(1)
    timeout = 5
    end_time = time.time() + timeout
    while True:
        try:
            email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
            # Nhập email vào ô input
            email_input.send_keys('hieuphp@gmail.com')
            email_input.send_keys(Keys.RETURN)
            break
        except Exception as e:
            # lỗi xử lý hàm
            print("Lỗi xử lý email")
            time.sleep(1)
        if time.time() > end_time:
            print("Lỗi thời gian tối đa email") 
            break    
    time.sleep(3)
    timeout = 5
    end_time = time.time() + timeout
    while True:
        try:
            pass_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
            # Nhập email vào ô input
            pass_input.send_keys('Admin12@')
            pass_input.send_keys(Keys.RETURN)
            break
        except Exception as e:
            # lỗi xử lý hàm
            print("Lỗi xử lý pass")
            time.sleep(1)
        if time.time() > end_time:
            print("Lỗi thời gian tối đa pass") 
            break  
    time.sleep(1)
    body_element = driver.find_element("tag name", "body").text  # Tìm thẻ <body>
    print("Nội dung văn bản của <body>:", body_element)
    all_windows = driver.window_handles
    
    # Chuyển sang cửa sổ mới (cửa sổ cuối cùng)
    driver.switch_to.window(all_windows[-1])

    # Thực hiện các thao tác trên cửa sổ mới
    print("Title của cửa sổ mới:", driver.title)

    # Chuyển về cửa sổ ban đầu
    driver.switch_to.window(all_windows[0])
    body_element = driver.find_element("tag name", "body").text  # Tìm thẻ <body>
    print("Nội dung văn bản của <body>:", body_element)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    title = driver.title
  
    driver.quit()
    return {
        "statusCode": 200,
        "body": f"{title}"
    }
