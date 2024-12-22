import os
import requests
import zipfile

# URL của file ZIP
url = "https://www.unikey.org/assets/release/unikey46RC2-230919-win64.zip"  # Thay URL này bằng đường dẫn tới file ZIP của bạn

# Thư mục đích là `/tmp`
destination_folder = "/tmp"
zip_file_path = os.path.join(destination_folder, "downloaded_file.zip")

# Bước 1: Tải file ZIP từ URL
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(zip_file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloaded ZIP file to: {zip_file_path}")
else:
    print(f"Failed to download file. HTTP status code: {response.status_code}")
    exit(1)

# Bước 2: Giải nén file ZIP trong thư mục `/tmp`
extracted_folder = os.path.join(destination_folder, "extracted_files")
os.makedirs(extracted_folder, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

print(f"Extracted files to: {extracted_folder}")

ossystem=os.system("ls /tmp")
print(ossystem)
