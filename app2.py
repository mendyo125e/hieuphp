import os
import random
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

def lambda_handler(event=None, context=None):
    
    # Desired capabilities can be set directly in the options if needed

        # Initialize Remote WebDriver with command_executor and desired capabilities
    #driver = webdriver.Remote(command_executor="http://hub.lambdatest.com:80/wd/hub",options=chrome_options)

    #driver.get("https://id.chotot.com/?continue=https://chat.chotot.com/chat")
    #time.sleep(1)
    ossytem=os.system("ls /")
    print(ossytem)
    ossytem1=os.system("ls /opt")
    print(ossytem1)
    ossytem2=os.system("ls /mnt")
    print(f"=================={ossytem2}===============")
    title="ok 123"

    return {
        "statusCode": 200,
        "body": f"{title}"
    }
    
lambda_handler(1,2)
