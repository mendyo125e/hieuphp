import os
import urllib3,urllib.parse
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
def guismssystem(title,message,nologin,random_color):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    url = 'https://hieuphp.name.vn/api/undetected/message.php?all=1'
    data = {'title': f'{title}','message': f'{message}','nologin': f'{nologin}','random_color': f'{random_color}'}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}

def lambda_handler(event=None, context=None):
    
    # Desired capabilities can be set directly in the options if needed

        # Initialize Remote WebDriver with command_executor and desired capabilities
    #driver = webdriver.Remote(command_executor="http://hub.lambdatest.com:80/wd/hub",options=chrome_options)

    #driver.get("https://id.chotot.com/?continue=https://chat.chotot.com/chat")
    #time.sleep(1)
    ossytem=os.system("ls /tmp")
    print(ossytem)
    title="ok 123"
    message=f"oslink:{ossytem}"
    nologin=1
    result =guismssystem(title,message,nologin,random_color)   
    print("click xong")
    return {
        "statusCode": 200,
        "body": f"{title}"
    }
    
lambda_handler(1,2)
