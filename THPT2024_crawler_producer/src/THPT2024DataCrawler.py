from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataCrawler:
    def __init__(self):
        # Cấu hình tùy chọn cho Firefox
        firefox_options = Options()
        firefox_options.add_argument('--headless')  # Chạy Firefox ở chế độ không có giao diện
        firefox_options.add_argument('--no-sandbox')  # Cần thiết khi chạy trong Docker
        firefox_options.add_argument('--disable-dev-shm-usage')  # Giảm thiểu vấn đề về bộ nhớ
        # Khởi tạo trình duyệt Firefox với các tùy chọn đã cấu hình
        self.driver = webdriver.Firefox(options=firefox_options)

    def open_page(self, url):
        """Mở trang web với thời gian chờ và thông báo trạng thái"""
        try:
            # Mở URL
            self.driver.get(url)
            
            # Tăng thời gian chờ để đảm bảo trang tải xong

            print(f"Truy cập thành công: {url}")
        except Exception as e:
            print(f"Không thể truy cập vào {url}. Lỗi: {e}")

    def find_element_by_css(self, css_selector):
        """Tìm và trả về phần tử bằng CSS selector"""
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            return element
        except Exception as e:
            print(f"Không thể tìm thấy phần tử: {e}")
            return None
    
    def extract_data(self):
        """Thu thập dữ liệu từ trang web"""
        try:
            # Tìm kiếm một phần tử trên trang (ví dụ, tìm theo thẻ h1)
            element = self.driver.find_element(By.TAG_NAME, 'h1')
            return element.text  # Trả về nội dung của thẻ h1
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def close_browser(self):
        """Đóng trình duyệt"""
        self.driver.quit()

def generate_number_string(n):
    # Đảm bảo phần số sau "37" luôn có 8 chữ số
    return f"37{n:06}"