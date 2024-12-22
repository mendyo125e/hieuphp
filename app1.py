def web_driver():

options = webdriver.ChromeOptions()

options.add_argument("--verbose")

options.add_argument('--no-sandbox')

options.add_argument('--headless')

options.add_argument('--disable-gpu')

options.add_argument("--window-size=1920, 1200")

options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

return driver

driver = web_driver()

import time

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver.get('https://accounts.google.com/')

time.sleep(1)

timeout = 10

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

print("Title của cửa sổ mới:", driver.title)

body_element = driver.find_element("tag name", "body").text # Tìm thẻ <body>

print("Nội dung văn bản của <body>:", body_element)

timeout = 10

end_time = time.time() + timeout

driver.quit()
