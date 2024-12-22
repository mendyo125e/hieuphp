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
    folder_name = "/home/my_render_folder"
    os.makedirs(folder_name, exist_ok=True)
    
    # Set quyền chmod 777
    os.chmod(folder_name, 0o777)
    
    # Tạo file trong folder
    file_path = os.path.join(folder_name, "example.txt")
    with open(file_path, "w") as file:
        file.write("Hello, this is a test file!")
    
    print(f"File '{file_path}' has been created!")
    ossytem=os.system("ls /")
    print(ossytem)
    ossytem1=os.system("ls /home/my_render_folder")
    print(ossytem1)
    ossytem2=os.system("ls /home")
    print(f"=================={ossytem2}===============")
    title="ok 123"

    return {
        "statusCode": 200,
        "body": f"{title}"
    }
    
lambda_handler(1,2)
