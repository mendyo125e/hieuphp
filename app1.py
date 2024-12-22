from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def lambda_handler(event=None, context=None):
    # Cấu hình trình duyệt
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy chế độ không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Khởi tạo WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        # Mở trang web
        driver.get("https://www.example.com")
        
        # Lấy tiêu đề trang
        title = driver.title
        
        # Đóng trình duyệt
        driver.quit()

        return {
            "statusCode": 200,
            "body": f"Title of the page is: {title}"
        }
    except Exception as e:
        driver.quit()
        return {
            "statusCode": 500,
            "body": f"Error occurred: {str(e)}"
        }
