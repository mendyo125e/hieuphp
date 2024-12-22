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
def random_color_by_name(testcolor):
    if testcolor=="test":
        color_names = [
            "blue", "green", "orange","red", "lightblue","grey","black","white" ,"yellow" ,"purple" ,"pink" ,"brown" ,"cyan","magenta","lime","gold","teal","navy","olive","maroon"       
        ]
    else:
        color_names = [
            "blue", "green", "orange","red", "lightblue","grey","black" 
        ]
    # Chọn ngẫu nhiên một màu
    return random.choice(color_names)
def guismssystem(title,message,nologin,random_color):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    url = 'https://hieuphp.name.vn/api/undetected/message.php?all=1'
    data = {'title': f'{title}','message': f'{message}','nologin': f'{nologin}','random_color': f'{random_color}'}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def lambda_handler1(event=None, context=None):
   print("test1")
def lambda_handler(event=None, context=None):
    
    random_color = random_color_by_name("test")
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
    title="ok 123"
    message="123456 jihihi"
    nologin=1
    result =guismssystem(title,message,nologin,random_color)   
    print("click xong")
    driver.quit()
    return {
        "statusCode": 200,
        "body": f"{title}"
    }
lambda_handler(1,2)
